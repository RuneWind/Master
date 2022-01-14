library(tidyverse)
library(ggplot2)

# Load hyperparameters that was used for training
hyps <- tibble(read_delim("hyperparameters.csv", delim = ";"))


  ##########################
###### TRAINING RESULTS ######
  ##########################

# Create data for storing collective data for all models and all epochs
train_results <- tibble("model_size"=character(), "model"=character(), "optimizer"=character(), "lr"=numeric(), "wd"=numeric(), "epoch"=numeric(), "train_box_loss"=numeric(),"train_obj_loss"=numeric(), "precision"=numeric(), "recall"=numeric(), "mAP_0.5"=numeric(), "mAP_0.75"=numeric(), "val_box_loss"=numeric(), "val_obj_loss"=numeric())
# Create dataframe for storing results from last epoch
yolo_results <- tibble("model_size"=c(rep("YOLOv5s", 18), rep("YOLOv5x", 18)), "model"=rep("0", 36), "optimizer"=rep("0", 36), "lr"=rep(-1, 36), "wd"=rep(-1, 36), "precision"=rep(-1, 36), "recall"=rep(-1, 36), "mAP_0.5"=rep(-1, 36), "mAP_0.75"=rep(-1, 36))

# Fill out the results dataframes with relevant information from training
for(i in seq(0, 17, 1)){
  model_s <- paste0("YOLOv5s", "_", formatC(i, width=2, format="d", flag="0"))
  model_x <- paste0("YOLOv5x", "_", formatC(i, width=2, format="d", flag="0"))
  
  sdf <- tibble(read_csv(paste0("YOLOv5s_results/", model_s, "_results/results.csv")))
  xdf <- tibble(read_csv(paste0("YOLOv5x_results/", model_x, "_results/results.csv")))
  
  # Fill yolo_results dataframe
  yolo_results[i+1, 2] <- model_s
  yolo_results[i+1, 3:5] <- hyps[i+1,]
  yolo_results[i+1, 6:9] <- sdf %>% filter(row_number() == nrow(sdf)) %>% select(c("metrics/precision", "metrics/recall", "metrics/mAP_0.5", "metrics/mAP_0.5:0.95")) %>% c()
  
  yolo_results[i+19, 2] <- model_x
  yolo_results[i+19, 3:5] <- hyps[i+1,]
  yolo_results[i+19, 6:9] <- xdf %>% filter(row_number() == nrow(xdf)) %>% select(c("metrics/precision", "metrics/recall", "metrics/mAP_0.5", "metrics/mAP_0.5:0.95")) %>% c()
  
  # Fill train_results dataframe
  sdf <- sdf %>% select(-c("train/cls_loss", "val/cls_loss", "x/lr0", "x/lr1", "x/lr2"))
  xdf <- xdf %>% select(-c("train/cls_loss", "val/cls_loss", "x/lr0", "x/lr1", "x/lr2"))
  
  sdf <- cbind(wd = hyps$weight_decay[i+1], sdf)
  sdf <- cbind(lr = hyps$learning_rate[i+1], sdf)
  sdf <- cbind(optimizer = hyps$optimizer[i+1], sdf)
  sdf <- cbind(model = model_s, sdf)
  sdf <- cbind(model_size = "YOLOv5s", sdf)
  
  xdf <- cbind(wd = hyps$weight_decay[i+1], xdf)
  xdf <- cbind(lr = hyps$learning_rate[i+1], xdf)
  xdf <- cbind(optimizer = hyps$optimizer[i+1], xdf)
  xdf <- cbind(model = model_x, xdf)
  xdf <- cbind(model_size = "YOLOv5x", xdf)
  
  colnames(train_results) <- colnames(xdf)
  train_results <- rbind(train_results, sdf, xdf)
  colnames(train_results)[7:14] <- c("train_bol_loss", "train_obj_loss", "precision", "recall", "map_0.5", "map_0.75_0.95", "val_box_loss", "val_obj_loss")
}

train_results$run <- substr(train_results$model, start=9, stop=10)

### Plots of yolo_results dataframe
ggplot(data = yolo_results) +
  geom_point(aes(x=log10(lr), y=mAP_0.75, colour=model_size, shape=optimizer), size=2) +
  facet_grid(.~wd)

ggplot(data = yolo_results[order(yolo_results$mAP_0.75, decreasing = TRUE), ][1:10, ]) +
  geom_point(aes(x=wd, y=mAP_0.75, color=as.factor(lr)), size=4) +
  facet_grid(.~optimizer)


### Plots of train_results dataframe
train_results$lr <- factor(train_results$lr, levels = c("2e-04", "0.001", "0.002", "0.01",  "0.05"),
                                              labels = c("lr=2e-04", "lr=1e-03", "lr=2e-03", "lr=1e-02", "lr=5e-02"))
train_results$wd <- factor(train_results$wd, levels = c("1e-04", "5e-04", "0.001"),
                                              labels = c("wd=1e-04", "wd=5e-04", "wd=1e-03"))


ggplot(data=train_results[train_results$epoch <= 150, ]) +
  geom_line(aes(x=epoch, y=map_0.75_0.95, color=optimizer, linetype=model_size), lwd=0.5) +
  facet_grid(wd~lr) +
  ylab("mAP_0.75:0.95") +
  xlab("Epochs") +
  theme_gray(base_size = 18)

ggplot(data=train_results[train_results$model == "YOLOv5x_11", ]) +
  geom_line(aes(x=epoch, y=map_0.75_0.95), color="red") +
  theme_grey() +
  xlab("Epochs") +
  ylab("mAP_0.75:0.95") +
  theme_gray(base_size = 15)

# Defailt models ARE THEY REALLY DEFAULTS????????
ggplot(data = train_results[train_results$run == "04" | train_results$run == "13", ]) +
  geom_line(aes(x=epoch, y=map_0.75_0.95, color=model_size), lwd=1) +
  facet_grid(.~optimizer) +
  theme_gray(base_size=15) +
  ylab("mAP_0.75:0.95") +
  xlab("Epochs")
  



  ######################
###### TEST RESULTS ######
  ######################
test_df <- read_csv("yolo_performance.csv")
test_df <- pivot_longer(test_df, cols = c("true_pos_0.10", "true_pos_0.50", "true_pos_0.75", "false_pos_0.10", "false_pos_0.50", "false_pos_0.75", "false_neg_0.10", "false_neg_0.50", "false_neg_0.75", "precision_0.10", "precision_0.50", "precision_0.75", "recall_0.10", "recall_0.50", "recall_0.75"),
                    names_to = c("metric", "threshold"), names_pattern = "([a-z]{4,5}[_][a-z]{3}|[a-z]{6,9})[_]([0-9][.][0-9]{2})")

ggplot(data=test_df[test_df$metric == "true_pos" & test_df$threshold == 0.75,]) +
  geom_col(aes(x = model, y = value)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

ggplot(data=test_df[test_df$threshold == 0.75 & test_df$metric %in% c("recall", "precision"), ]) +
  geom_histogram(aes(x=value), color="grey3", fill="skyblue", bins = 100) +
  facet_grid(metric~.) +
  theme_gray(base_size = 15) +
  xlim(0,1)


# IoU results
iou_df <- read_csv("iou_df.csv")
iou_df <- pivot_longer(iou_df, cols=colnames(iou_df), names_to="model", values_to="iou")
iou_df <- iou_df[!is.na(iou_df$iou), ]

iou_df$model_size <- substr(iou_df$model, start=1, stop=7)
iou_df$Optimizer <- ifelse(substr(iou_df$model, start=9, stop=10) %in% c("00", "01", "02", "03", "04", "05", "06", "07", "08"), yes="SGD", no="adam")
iou_df$run <- substr(iou_df$model, start=9, stop=10)

ggplot(data=iou_df) +
  geom_histogram(aes(x=iou), bins = 40, color="grey3", fill="skyblue")


ggplot(data = iou_df) +
  geom_boxplot(aes(y=iou, x=model)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

levels(iou_df$run) <- c("00", "01", "02", "03", "SGD Default", "05", "06", "07", "08", "09", "10", "Best", "12", "13", "adam Default", "15", "Worst", "17")
ggplot(data=iou_df[iou_df$model %in% c("YOLOv5x_11", "YOLOv5x_16", "YOLOv5s_04", "YOLOv5x_04", "YOLOv5s_14", "YOLOv5x_14"), ]) +
  geom_boxplot(aes(y=iou, x=model, color=Optimizer)) +
  # facet_wrap(~run, scales = "free", labeller = as_labeller(levels(iou_df$run))) +
  xlab("Model") +
  ylab("IoU")




















