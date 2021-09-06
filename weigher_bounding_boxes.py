"""Weigher bounding boxes (left_x, top_y, width, height) for firefly's.

The timestamp associated with the bounding boxes represents the earliest/first recorded time.
"""
from dataclasses import dataclass

import pandas as pd

from nippon.logging import logger


@dataclass
class BoundingBox:
    """Holding bounding box coordinates."""

    x: int
    y: int
    width: int
    height: int


WEIGHER_BOUNDING_BOXES = {
    "0a:92:5e:29:ec:a2": [
        ("20191223T000000+0900", (660, 388, 125, 125)),
        ("20200109T112152+0900", (625, 364, 125, 125)),
        ("20200111T154248+0900", (625, 359, 125, 125)),
        ("20200122T083237+0900", (621, 356, 125, 125)),
        ("20200129T152237+0900", (621, 353, 125, 125)),
        ("20200306T073915+0900", (623, 355, 125, 125)),
        ("20200324T025619+0900", (509, 371, 125, 125)),
        ("20200324T154849+0900", (494, 364, 125, 125)),
        ("20200403T041917+0900", (589, 386, 125, 125)),
        ("20200406T020716+0900", (600, 350, 125, 125)),
        ("20200623T000156+0900", (531, 299, 125, 125)),
        ("20200628T160847+0900", (553, 340, 125, 125)),
        ("20200630T135413+0900", (557, 354, 125, 125)),
        ("20200702T151443+0900", (558, 359, 125, 125)),
        ("20200709T133145+0900", (594, 394, 125, 125)),
        ("20200726T181142+0900", (554, 359, 125, 125)),
        ("20200801T111630+0900", (548, 345, 125, 125)),
        ("20200806T083324+0900", (553, 317, 125, 125)),
        ("20200908T153420+0900", (537, 290, 125, 125)),
        ("20200910T134646+0900", (536, 272, 125, 125)),
        ("20200922T141552+0900", (535, 261, 125, 125)),
    ],
    "92:f0:4a:67:37:cb": [
        ("20191223T000000+0900", (718, 360, 124, 124)),
        ("20200109T144642+0900", (700, 382, 124, 124)),
        ("20200623T092214+0900", (550, 327, 124, 124)),
        ("20200623T093733+0900", (550, 331, 124, 124)),
        ("20200623T104902+0900", (542, 328, 124, 124)),
        ("20200623T132730+0900", (538, 339, 124, 124)),
        ("20200629T131709+0900", (550, 304, 124, 124)),
        ("20200630T163740+0900", (559, 264, 124, 124)),
        ("20200702T140915+0900", (562, 255, 124, 124)),
        ("20200704T164102+0900", (557, 258, 124, 124)),
        ("20200709T224613+0900", (540, 247, 124, 124)),
        ("20200711T160205+0900", (542, 255, 124, 124)),
        ("20200713T082452+0900", (544, 263, 124, 124)),
        ("20200715T134009+0900", (537, 253, 124, 124)),
        ("20200721T155750+0900", (538, 286, 124, 124)),
        ("20200724T082734+0900", (541, 280, 124, 124)),
        ("20200803T082246+0900", (533, 276, 124, 124)),
        ("20200806T152104+0900", (531, 314, 124, 124)),
        ("20200918T083103+0900", (547, 297, 124, 124)),
        ("20200919T081946+0900", (539, 292, 124, 124)),
        ("20200919T122625+0900", (542, 293, 124, 124)),
        ("20201006T141318+0900", (527, 278, 124, 124)),
        ("20201008T110155+0900", (522, 285, 124, 124)),
        ("20201008T142559+0900", (518, 290, 124, 124)),
        ("20201012T084948+0900", (511, 298, 124, 124)),
    ],
    "7a:08:0a:9a:38:75": [
        ("20191223T000000+0900", (579, 226, 109, 109)),
        ("20191231T100656+0900", (616, 207, 109, 109)),
        ("20200108T100256+0900", (630, 205, 109, 109)),
        ("20200108T101309+0900", (660, 209, 109, 109)),
        ("20200127T084951+0900", (659, 206, 109, 109)),
        ("20200217T133254+0900", (662, 203, 109, 109)),
        ("20200217T133759+0900", (0, 0, 109, 109)),  # No weigher
        ("20200217T134305+0900", (665, 270, 109, 109)),
        ("20200222T054833+0900", (661, 268, 109, 109)),
        ("20200226T143159+0900", (650, 244, 109, 109)),
        ("20200227T074720+0900", (648, 224, 109, 109)),
        ("20200228T193131+0900", (643, 230, 109, 109)),
        ("20200229T134841+0900", (645, 224, 109, 109)),
        ("20200316T143300+0900", (634, 227, 109, 109)),
        ("20200327T083853+0900", (816, 150, 109, 109)),
        ("20200323T141526+0900", (818, 165, 109, 109)),
        ("20200331T123752+0900", (794, 242, 109, 109)),
        ("20200417T053146+0900", (792, 237, 109, 109)),
        ("20200619T201149+0900", (592, 305, 109, 109)),
        ("20200701T083118+0900", (605, 292, 109, 109)),
        ("20200813T082126+0900", (603, 280, 109, 109)),
        ("20200813T083801+0900", (603, 272, 109, 109)),
        ("20200817T140320+0900", (613, 270, 109, 109)),
        ("20200819T081248+0900", (611, 263, 109, 109)),
        ("20200821T105717+0900", (596, 264, 109, 109)),
        ("20200831T132051+0900", (592, 260, 109, 109)),
        ("20200901T110137+0900", (576, 260, 109, 109)),
        ("20200902T131122+0900", (574, 265, 109, 109)),
        ("20200904T161116+0900", (578, 249, 109, 109)),
        ("20200914T135050+0900", (0, 0, 109, 109)),  # No weigher
        ("20200914T135835+0900", (595, 236, 109, 109)),
        ("20200914T155414+0900", (598, 225, 109, 109)),
        ("20201018T082257+0900", (641, 188, 109, 109)),
    ],
    "42:de:f3:4e:40:f7": [
        ("20191223T000000+0900", (511, 302, 108, 108)),
        ("20191227T135308+0900", (515, 298, 108, 108)),
        ("20200217T135346+0900", (558, 267, 108, 108)),
        ("20200309T135532+0900", (549, 228, 108, 108)),
        ("20200309T142604+0900", (596, 221, 108, 108)),
        ("20200312T140234+0900", (580, 209, 108, 108)),
        ("20200323T142856+0900", (525, 209, 108, 108)),
        ("20200619T015621+0900", (550, 297, 108, 108)),
        ("20200630T084308+0900", (558, 291, 108, 108)),
        ("20200911T113816+0900", (581, 273, 108, 108)),
        ("20200914T141036+0900", (607, 277, 108, 108)),
        ("20201019T130008+0900", (609, 244, 108, 108)),
    ],
    "ce:2d:09:db:50:bc": [
        ("20191223T000000+0900", (634, 219, 111, 111)),
        ("20200107T124810+0900", (717, 169, 111, 111)),
        ("20200217T144933+0900", (584, 201, 111, 111)),
        ("20200219T142336+0900", (563, 219, 111, 111)),
        ("20200222T113758+0900", (549, 215, 111, 111)),
        ("20200306T142404+0900", (514, 191, 111, 111)),
        ("20200307T090024+0900", (522, 192, 111, 111)),
        ("20200327T111356+0900", (463, 161, 111, 111)),
        ("20200619T035557+0900", (592, 230, 111, 111)),
        ("20200623T113946+0900", (597, 226, 111, 111)),
        ("20200714T172200+0900", (597, 227, 111, 111)),
        ("20200816T084800+0900", (599, 227, 111, 111)),
        ("20200831T205824+0900", (594, 229, 111, 111)),
        ("20200914T092100+0900", (614, 218, 111, 111)),
        ("20200914T142743+0900", (0, 0, 109, 109)),  # No weigher
        ("20200914T143103+0900", (587, 220, 111, 111)),
        ("20201007T061518+0900", (597, 209, 111, 111)),
    ],
    "d6:16:e0:3b:ed:c4": [
        ("20191223T000000+0900", (510, 282, 112, 110)),
        ("20200217T145036+0900", (545, 272, 112, 110)),
        ("20200222T141326+0900", (534, 210, 112, 110)),
        ("20200309T154000+0900", (650, 228, 112, 110)),
        ("20200623T010311+0900", (575, 291, 112, 110)),
        ("20200701T122643+0900", (0, 0, 109, 109)),  # No weigher
        ("20200707T084429+0900", (515, 223, 112, 110)),
        ("20200708T155613+0900", (544, 282, 112, 110)),
        ("20200713T085923+0900", (594, 270, 112, 110)),
        ("20200914T144537+0900", (0, 0, 109, 109)),  # No weigher
        ("20200916T085749+0900", (484, 253, 112, 110)),
        ("20200916T135314+0900", (0, 0, 109, 109)),  # No weigher
        ("20200916T140106+0900", (585, 276, 109, 109)),
        ("20200919T094857+0900", (592, 275, 109, 109)),
        ("20200928T143334+0900", (0, 0, 109, 109)),  # No weigher
        ("20200928T144545+0900", (524, 316, 112, 110)),
        ("20200929T084802+0900", (549, 292, 112, 110)),
        ("20200929T093803+0900", (557, 287, 112, 110)),
        ("20201006T085246+0900", (563, 264, 112, 110)),
        ("20201011T121053+0900", (592, 219, 112, 110)),
        ("20201011T122417+0900", (594, 212, 112, 110)),
        ("20201012T110500+0900", (580, 217, 112, 110)),
        ("20201019T071530+0900", (613, 189, 112, 110)),
    ],
    "86:c1:6e:2b:5b:53": [
        ("20191223T000000+0900", (673, 412, 109, 109)),
        ("20200121T133934+0900", (675, 415, 109, 109)),
        ("20200205T091920+0900", (603, 365, 109, 109)),
        ("20200228T010726+0900", (605, 366, 109, 109)),
        ("20200309T160738+0900", (642, 366, 109, 109)),
        ("20200405T085809+0900", (565, 455, 109, 109)),
        ("20200406T153721+0900", (570, 455, 109, 109)),
        ("20200407T124649+0900", (602, 329, 109, 109)),
        ("20200408T091933+0900", (610, 337, 109, 109)),
        ("20200409T090539+0900", (616, 339, 109, 109)),
        ("20200629T100325+0900", (587, 356, 109, 109)),
        ("20200703T090541+0900", (588, 360, 109, 109)),
        ("20200716T082200+0900", (595, 397, 109, 109)),
        ("20200729T112224+0900", (581, 399, 109, 109)),
        ("20200811T154529+0900", (568, 405, 109, 109)),
        ("20200817T144824+0900", (573, 403, 109, 109)),
        ("20200824T095216+0900", (578, 402, 109, 109)),
        ("20200914T133059+0900", (0, 0, 109, 109)),  # No weigher
        ("20200914T161541+0900", (720, 359, 109, 109)),
        ("20200915T094101+0900", (727, 363, 109, 109)),
        ("20200915T094418+0900", (727, 368, 109, 109)),
        ("20200915T111350+0900", (721, 366, 109, 109)),
        ("20200916T071110+0900", (729, 369, 109, 109)),
        ("20200916T091846+0900", (743, 378, 109, 109)),
        ("20200918T133248+0900", (0, 0, 109, 109)),  # No weigher
        ("20200919T092440+0900", (670, 405, 109, 109)),
        ("20200926T132244+0900", (648, 422, 109, 109)),
        ("20200929T161858+0900", (655, 424, 109, 109)),
    ],
    "12:96:29:e0:dd:19": [
        ("20191223T000000+0900", (578, 317, 115, 114)),
        ("20200108T143422+0900", (577, 325, 115, 114)),
        ("20200310T070320+0900", (678, 322, 115, 114)),
        ("20200616T195444+0900", (592, 324, 115, 114)),
        ("20200701T034142+0900", (585, 324, 115, 114)),
        ("20200709T093734+0900", (570, 350, 115, 114)),
        ("20200909T140220+0900", (462, 373, 115, 114)),
        ("20200914T134800+0900", (0, 0, 109, 109)),
        ("20200914T161630+0900", (626, 356, 115, 114)),
        ("20200924T094313+0900", (792, 469, 115, 114)),
        ("20200924T094419+0900", (665, 419, 115, 114)),
    ],
    "1a:1c:70:4d:ee:5d": [
        ("20191223T000000+0900", (545, 377, 109, 109)),
        ("20191224T084943+0900", (546, 373, 109, 109)),
        ("20200122T094858+0900", (555, 311, 109, 109)),
        ("20200128T113510+0900", (587, 336, 109, 109)),
        ("20200131T113510+0900", (581, 335, 109, 109)),
        ("20200204T132316+0900", (593, 330, 109, 109)),
        ("20200211T162155+0900", (612, 330, 109, 109)),
        ("20200227T004340+0900", (619, 326, 109, 109)),
        ("20200227T095242+0900", (616, 327, 109, 109)),
        ("20200227T095749+0900", (653, 212, 109, 109)),
        ("20200227T095749+0900", (654, 214, 109, 109)),
        ("20200227T142739+0900", (653, 213, 109, 109)),
        ("20200324T084117+0900", (717, 368, 109, 109)),
        ("20200327T093736+0900", (906, 368, 109, 109)),
        ("20200407T104047+0900", (855, 366, 109, 109)),
        ("20200407T120215+0900", (856, 363, 109, 109)),
        ("20200408T105806+0900", (835, 353, 109, 109)),
        ("20200409T133730+0900", (835, 355, 109, 109)),
        ("20200622T152742+0900", (590, 319, 111, 111)),
        ("20200729T085253+0900", (585, 336, 105, 106)),
        ("20200729T092408+0900", (0, 0, 109, 109)),  # No weigher
        ("20200801T093206+0900", (615, 297, 113, 110)),
        ("20200827T083723+0900", (0, 0, 109, 109)),  # No weigher
        ("20200827T083936+0900", (1145, 281, 122, 112)),
        ("20200828T111927+0900", (1107, 278, 113, 110)),
        ("20200829T094400+0900", (453, 352, 113, 112)),
        ("20200831T095516+0900", (474, 350, 113, 109)),
        ("20200903T131938+0900", (478, 344, 113, 109)),
        ("20200914T143124+0900", (0, 0, 109, 109)),  # No weigher
        ("20200914T154947+0900", (608, 505, 122, 111)),
        ("20200916T092539+0900", (631, 319, 113, 109)),
        ("20200927T135946+0900", (0, 0, 109, 109)),  # No weigher
        ("20200927T142147+0900", (485, 262, 113, 109)),
        ("20200928T093417+0900", (586, 443, 113, 109)),
        ("20201008T083758+0900", (552, 340, 113, 109)),
        ("20201009T092833+0900", (541, 367, 113, 109)),
    ],
    "2a:18:f9:6e:b1:c2": [
        ("20191223T000000+0900", (617, 314, 109, 109)),
        ("20191225T090046+0900", (620, 318, 109, 109)),
        ("20191225T142103+0900", (627, 325, 109, 109)),
        ("20191227T090327+0900", (630, 324, 109, 109)),
        ("20200108T111536+0900", (623, 321, 109, 109)),
        ("20200108T114105+0900", (621, 331, 109, 109)),
        ("20200108T114611+0900", (608, 332, 109, 109)),
        ("20200108T141347+0900", (616, 323, 109, 109)),
        ("20200128T133316+0900", (261, 502, 109, 109)),
        ("20200128T141905+0900", (453, 295, 109, 109)),
        ("20200201T094343+0900", (438, 296, 109, 109)),
        ("20200206T091657+0900", (447, 303, 109, 109)),
        ("20200227T082236+0900", (296, 131, 109, 109)),
        ("20200229T090002+0900", (621, 310, 109, 109)),
        ("20200309T104152+0900", (626, 313, 109, 109)),
        ("20200309T111727+0900", (686, 298, 109, 109)),
        ("20200327T141325+0900", (536, 359, 109, 109)),
        ("20200405T142422+0900", (705, 323, 109, 109)),
        ("20200406T160205+0900", (701, 328, 109, 109)),
        ("20200407T084117+0900", (691, 338, 109, 109)),
        ("20200410T212454+0900", (690, 335, 109, 109)),
        ("20200619T035058+0900", (525, 318, 109, 109)),
        ("20200622T152746+0900", (535, 324, 109, 109)),
        ("20200623T100228+0900", (566, 342, 109, 109)),
        ("20200625T091313+0900", (555, 347, 109, 109)),
        ("20200702T132759+0900", (555, 358, 109, 109)),
        ("20200716T113231+0900", (573, 379, 109, 109)),
        ("20200729T143436+0900", (635, 404, 109, 109)),
        ("20200827T094749+0900", (0, 0, 109, 109)),  # No weigher
        ("20200829T094412+0900", (321, 305, 109, 109)),
        ("20200916T093537+0900", (534, 332, 109, 109)),
        ("20200919T141607+0900", (0, 0, 109, 109)),  # No weigher
        ("20200919T143241+0900", (494, 277, 109, 109)),
        ("20200927T135212+0900", (0, 0, 109, 109)),  # No weigher
        ("20200927T135422+0900", (592, 405, 109, 109)),
        ("20200928T090326+0900", (593, 408, 109, 109)),
        ("20200928T095835+0900", (597, 413, 109, 109)),
    ],
}


def weigher_bounding_boxes_dataframe(as_array: bool = True) -> pd.DataFrame:
    """Create data frame from raw bounding boxes dictionary."""
    weigher_bounding_boxes = []
    for fid, timestamp_bounding_box in WEIGHER_BOUNDING_BOXES.items():
        bounding_boxes = pd.DataFrame(timestamp_bounding_box, columns=["Timestamp", "WeigherBoundingBox"])
        bounding_boxes["DeviceId"] = fid.replace(":", "-")
        weigher_bounding_boxes.append(bounding_boxes)
    df_bounding_boxes = pd.concat(weigher_bounding_boxes)
    if not as_array:
        logger.info("Transforming bounding boxes to BoundingBox dataclass")
        df_bounding_boxes["WeigherBoundingBox"].apply(lambda x: BoundingBox(*x))
    df_bounding_boxes["Timestamp"] = pd.to_datetime(df_bounding_boxes["Timestamp"]).dt.tz_convert("Asia/Tokyo")
    df_bounding_boxes.sort_values("Timestamp", inplace=True)
    df_bounding_boxes.set_index("Timestamp", inplace=True)
    df_bounding_boxes["DeviceId"] = df_bounding_boxes["DeviceId"].astype("category")

    return df_bounding_boxes


def add_weigher_bounding_boxes(df: pd.DataFrame) -> pd.DataFrame:
    """Add bounding boxes to input data frame.

    Merging input data frame with bounding box data frame by device id and index timestamp (backwards).
    """
    df_bounding_boxes = weigher_bounding_boxes_dataframe()
    df_bounding_boxes_at_ids = df_bounding_boxes[df_bounding_boxes["DeviceId"].isin(df["DeviceId"])]
    df_bounding_boxes_at_ids["DeviceId"].cat.remove_unused_categories(inplace=True)
    df.sort_index(inplace=True)
    df_with_bounding_boxes = pd.merge_asof(
        df, df_bounding_boxes_at_ids, left_index=True, right_index=True, by="DeviceId", direction="backward"
    )
    return df_with_bounding_boxes
