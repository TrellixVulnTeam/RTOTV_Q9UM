# -*- coding: utf-8 -*-

# MySQL Connector/Python - MySQL driver written in Python.
# Copyright (c) 2013, Oracle and/or its affiliates. All rights reserved.

# MySQL Connector/Python is licensed under the terms of the GPLv2
# <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>, like most
# MySQL Connectors. There are special exceptions to the terms and
# conditions of the GPLv2 as it is applied to this software, see the
# FOSS License Exception
# <http://www.mysql.com/about/legal/licensing/foss-exception.html>.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA 

# This file was auto-generated.
_GENERATED_ON = '2013-10-04'
_MYSQL_VERSION = (5, 7, 2)

"""This module contains the MySQL Server and Client error codes"""

# Start MySQL Errors
ER_HASHCHK = 1000
ER_NISAMCHK = 1001
ER_NO = 1002
ER_YES = 1003
ER_CANT_CREATE_FILE = 1004
ER_CANT_CREATE_TABLE = 1005
ER_CANT_CREATE_DB = 1006
ER_DB_CREATE_EXISTS = 1007
ER_DB_DROP_EXISTS = 1008
ER_DB_DROP_DELETE = 1009
ER_DB_DROP_RMDIR = 1010
ER_CANT_DELETE_FILE = 1011
ER_CANT_FIND_SYSTEM_REC = 1012
ER_CANT_GET_STAT = 1013
ER_CANT_GET_WD = 1014
ER_CANT_LOCK = 1015
ER_CANT_OPEN_FILE = 1016
ER_FILE_NOT_FOUND = 1017
ER_CANT_READ_DIR = 1018
ER_CANT_SET_WD = 1019
ER_CHECKREAD = 1020
ER_DISK_FULL = 1021
ER_DUP_KEY = 1022
ER_ERROR_ON_CLOSE = 1023
ER_ERROR_ON_READ = 1024
ER_ERROR_ON_RENAME = 1025
ER_ERROR_ON_WRITE = 1026
ER_FILE_USED = 1027
ER_FILSORT_ABORT = 1028
ER_FORM_NOT_FOUND = 1029
ER_GET_ERRNO = 1030
ER_ILLEGAL_HA = 1031
ER_KEY_NOT_FOUND = 1032
ER_NOT_FORM_FILE = 1033
ER_NOT_KEYFILE = 1034
ER_OLD_KEYFILE = 1035
ER_OPEN_AS_READONLY = 1036
ER_OUTOFMEMORY = 1037
ER_OUT_OF_SORTMEMORY = 1038
ER_UNEXPECTED_EOF = 1039
ER_CON_COUNT_ERROR = 1040
ER_OUT_OF_RESOURCES = 1041
ER_BAD_HOST_ERROR = 1042
ER_HANDSHAKE_ERROR = 1043
ER_DBACCESS_DENIED_ERROR = 1044
ER_ACCESS_DENIED_ERROR = 1045
ER_NO_DB_ERROR = 1046
ER_UNKNOWN_COM_ERROR = 1047
ER_BAD_NULL_ERROR = 1048
ER_BAD_DB_ERROR = 1049
ER_TABLE_EXISTS_ERROR = 1050
ER_BAD_TABLE_ERROR = 1051
ER_NON_UNIQ_ERROR = 1052
ER_SERVER_SHUTDOWN = 1053
ER_BAD_FIELD_ERROR = 1054
ER_WRONG_FIELD_WITH_GROUP = 1055
ER_WRONG_GROUP_FIELD = 1056
ER_WRONG_SUM_SELECT = 1057
ER_WRONG_VALUE_COUNT = 1058
ER_TOO_LONG_IDENT = 1059
ER_DUP_FIELDNAME = 1060
ER_DUP_KEYNAME = 1061
ER_DUP_ENTRY = 1062
ER_WRONG_FIELD_SPEC = 1063
ER_PARSE_ERROR = 1064
ER_EMPTY_QUERY = 1065
ER_NONUNIQ_TABLE = 1066
ER_INVALID_DEFAULT = 1067
ER_MULTIPLE_PRI_KEY = 1068
ER_TOO_MANY_KEYS = 1069
ER_TOO_MANY_KEY_PARTS = 1070
ER_TOO_LONG_KEY = 1071
ER_KEY_COLUMN_DOES_NOT_EXITS = 1072
ER_BLOB_USED_AS_KEY = 1073
ER_TOO_BIG_FIELDLENGTH = 1074
ER_WRONG_AUTO_KEY = 1075
ER_READY = 1076
ER_NORMAL_SHUTDOWN = 1077
ER_GOT_SIGNAL = 1078
ER_SHUTDOWN_COMPLETE = 1079
ER_FORCING_CLOSE = 1080
ER_IPSOCK_ERROR = 1081
ER_NO_SUCH_INDEX = 1082
ER_WRONG_FIELD_TERMINATORS = 1083
ER_BLOBS_AND_NO_TERMINATED = 1084
ER_TEXTFILE_NOT_READABLE = 1085
ER_FILE_EXISTS_ERROR = 1086
ER_LOAD_INFO = 1087
ER_ALTER_INFO = 1088
ER_WRONG_SUB_KEY = 1089
ER_CANT_REMOVE_ALL_FIELDS = 1090
ER_CANT_DROP_FIELD_OR_KEY = 1091
ER_INSERT_INFO = 1092
ER_UPDATE_TABLE_USED = 1093
ER_NO_SUCH_THREAD = 1094
ER_KILL_DENIED_ERROR = 1095
ER_NO_TABLES_USED = 1096
ER_TOO_BIG_SET = 1097
ER_NO_UNIQUE_LOGFILE = 1098
ER_TABLE_NOT_LOCKED_FOR_WRITE = 1099
ER_TABLE_NOT_LOCKED = 1100
ER_BLOB_CANT_HAVE_DEFAULT = 1101
ER_WRONG_DB_NAME = 1102
ER_WRONG_TABLE_NAME = 1103
ER_TOO_BIG_SELECT = 1104
ER_UNKNOWN_ERROR = 1105
ER_UNKNOWN_PROCEDURE = 1106
ER_WRONG_PARAMCOUNT_TO_PROCEDURE = 1107
ER_WRONG_PARAMETERS_TO_PROCEDURE = 1108
ER_UNKNOWN_TABLE = 1109
ER_FIELD_SPECIFIED_TWICE = 1110
ER_INVALID_GROUP_FUNC_USE = 1111
ER_UNSUPPORTED_EXTENSION = 1112
ER_TABLE_MUST_HAVE_COLUMNS = 1113
ER_RECORD_FILE_FULL = 1114
ER_UNKNOWN_CHARACTER_SET = 1115
ER_TOO_MANY_TABLES = 1116
ER_TOO_MANY_FIELDS = 1117
ER_TOO_BIG_ROWSIZE = 1118
ER_STACK_OVERRUN = 1119
ER_WRONG_OUTER_JOIN = 1120
ER_NULL_COLUMN_IN_INDEX = 1121
ER_CANT_FIND_UDF = 1122
ER_CANT_INITIALIZE_UDF = 1123
ER_UDF_NO_PATHS = 1124
ER_UDF_EXISTS = 1125
ER_CANT_OPEN_LIBRARY = 1126
ER_CANT_FIND_DL_ENTRY = 1127
ER_FUNCTION_NOT_DEFINED = 1128
ER_HOST_IS_BLOCKED = 1129
ER_HOST_NOT_PRIVILEGED = 1130
ER_PASSWORD_ANONYMOUS_USER = 1131
ER_PASSWORD_NOT_ALLOWED = 1132
ER_PASSWORD_NO_MATCH = 1133
ER_UPDATE_INFO = 1134
ER_CANT_CREATE_THREAD = 1135
ER_WRONG_VALUE_COUNT_ON_ROW = 1136
ER_CANT_REOPEN_TABLE = 1137
ER_INVALID_USE_OF_NULL = 1138
ER_REGEXP_ERROR = 1139
ER_MIX_OF_GROUP_FUNC_AND_FIELDS = 1140
ER_NONEXISTING_GRANT = 1141
ER_TABLEACCESS_DENIED_ERROR = 1142
ER_COLUMNACCESS_DENIED_ERROR = 1143
ER_ILLEGAL_GRANT_FOR_TABLE = 1144
ER_GRANT_WRONG_HOST_OR_USER = 1145
ER_NO_SUCH_TABLE = 1146
ER_NONEXISTING_TABLE_GRANT = 1147
ER_NOT_ALLOWED_COMMAND = 1148
ER_SYNTAX_ERROR = 1149
ER_UNUSED1 = 1150
ER_UNUSED2 = 1151
ER_ABORTING_CONNECTION = 1152
ER_NET_PACKET_TOO_LARGE = 1153
ER_NET_READ_ERROR_FROM_PIPE = 1154
ER_NET_FCNTL_ERROR = 1155
ER_NET_PACKETS_OUT_OF_ORDER = 1156
ER_NET_UNCOMPRESS_ERROR = 1157
ER_NET_READ_ERROR = 1158
ER_NET_READ_INTERRUPTED = 1159
ER_NET_ERROR_ON_WRITE = 1160
ER_NET_WRITE_INTERRUPTED = 1161
ER_TOO_LONG_STRING = 1162
ER_TABLE_CANT_HANDLE_BLOB = 1163
ER_TABLE_CANT_HANDLE_AUTO_INCREMENT = 1164
ER_UNUSED3 = 1165
ER_WRONG_COLUMN_NAME = 1166
ER_WRONG_KEY_COLUMN = 1167
ER_WRONG_MRG_TABLE = 1168
ER_DUP_UNIQUE = 1169
ER_BLOB_KEY_WITHOUT_LENGTH = 1170
ER_PRIMARY_CANT_HAVE_NULL = 1171
ER_TOO_MANY_ROWS = 1172
ER_REQUIRES_PRIMARY_KEY = 1173
ER_NO_RAID_COMPILED = 1174
ER_UPDATE_WITHOUT_KEY_IN_SAFE_MODE = 1175
ER_KEY_DOES_NOT_EXITS = 1176
ER_CHECK_NO_SUCH_TABLE = 1177
ER_CHECK_NOT_IMPLEMENTED = 1178
ER_CANT_DO_THIS_DURING_AN_TRANSACTION = 1179
ER_ERROR_DURING_COMMIT = 1180
ER_ERROR_DURING_ROLLBACK = 1181
ER_ERROR_DURING_FLUSH_LOGS = 1182
ER_ERROR_DURING_CHECKPOINT = 1183
ER_NEW_ABORTING_CONNECTION = 1184
ER_DUMP_NOT_IMPLEMENTED = 1185
ER_FLUSH_MASTER_BINLOG_CLOSED = 1186
ER_INDEX_REBUILD = 1187
ER_MASTER = 1188
ER_MASTER_NET_READ = 1189
ER_MASTER_NET_WRITE = 1190
ER_FT_MATCHING_KEY_NOT_FOUND = 1191
ER_LOCK_OR_ACTIVE_TRANSACTION = 1192
ER_UNKNOWN_SYSTEM_VARIABLE = 1193
ER_CRASHED_ON_USAGE = 1194
ER_CRASHED_ON_REPAIR = 1195
ER_WARNING_NOT_COMPLETE_ROLLBACK = 1196
ER_TRANS_CACHE_FULL = 1197
ER_SLAVE_MUST_STOP = 1198
ER_SLAVE_NOT_RUNNING = 1199
ER_BAD_SLAVE = 1200
ER_MASTER_INFO = 1201
ER_SLAVE_THREAD = 1202
ER_TOO_MANY_USER_CONNECTIONS = 1203
ER_SET_CONSTANTS_ONLY = 1204
ER_LOCK_WAIT_TIMEOUT = 1205
ER_LOCK_TABLE_FULL = 1206
ER_READ_ONLY_TRANSACTION = 1207
ER_DROP_DB_WITH_READ_LOCK = 1208
ER_CREATE_DB_WITH_READ_LOCK = 1209
ER_WRONG_ARGUMENTS = 1210
ER_NO_PERMISSION_TO_CREATE_USER = 1211
ER_UNION_TABLES_IN_DIFFERENT_DIR = 1212
ER_LOCK_DEADLOCK = 1213
ER_TABLE_CANT_HANDLE_FT = 1214
ER_CANNOT_ADD_FOREIGN = 1215
ER_NO_REFERENCED_ROW = 1216
ER_ROW_IS_REFERENCED = 1217
ER_CONNECT_TO_MASTER = 1218
ER_QUERY_ON_MASTER = 1219
ER_ERROR_WHEN_EXECUTING_COMMAND = 1220
ER_WRONG_USAGE = 1221
ER_WRONG_NUMBER_OF_COLUMNS_IN_SELECT = 1222
ER_CANT_UPDATE_WITH_READLOCK = 1223
ER_MIXING_NOT_ALLOWED = 1224
ER_DUP_ARGUMENT = 1225
ER_USER_LIMIT_REACHED = 1226
ER_SPECIFIC_ACCESS_DENIED_ERROR = 1227
ER_LOCAL_VARIABLE = 1228
ER_GLOBAL_VARIABLE = 1229
ER_NO_DEFAULT = 1230
ER_WRONG_VALUE_FOR_VAR = 1231
ER_WRONG_TYPE_FOR_VAR = 1232
ER_VAR_CANT_BE_READ = 1233
ER_CANT_USE_OPTION_HERE = 1234
ER_NOT_SUPPORTED_YET = 1235
ER_MASTER_FATAL_ERROR_READING_BINLOG = 1236
ER_SLAVE_IGNORED_TABLE = 1237
ER_INCORRECT_GLOBAL_LOCAL_VAR = 1238
ER_WRONG_FK_DEF = 1239
ER_KEY_REF_DO_NOT_MATCH_TABLE_REF = 1240
ER_OPERAND_COLUMNS = 1241
ER_SUBQUERY_NO_1_ROW = 1242
ER_UNKNOWN_STMT_HANDLER = 1243
ER_CORRUPT_HELP_DB = 1244
ER_CYCLIC_REFERENCE = 1245
ER_AUTO_CONVERT = 1246
ER_ILLEGAL_REFERENCE = 1247
ER_DERIVED_MUST_HAVE_ALIAS = 1248
ER_SELECT_REDUCED = 1249
ER_TABLENAME_NOT_ALLOWED_HERE = 1250
ER_NOT_SUPPORTED_AUTH_MODE = 1251
ER_SPATIAL_CANT_HAVE_NULL = 1252
ER_COLLATION_CHARSET_MISMATCH = 1253
ER_SLAVE_WAS_RUNNING = 1254
ER_SLAVE_WAS_NOT_RUNNING = 1255
ER_TOO_BIG_FOR_UNCOMPRESS = 1256
ER_ZLIB_Z_MEM_ERROR = 1257
ER_ZLIB_Z_BUF_ERROR = 1258
ER_ZLIB_Z_DATA_ERROR = 1259
ER_CUT_VALUE_GROUP_CONCAT = 1260
ER_WARN_TOO_FEW_RECORDS = 1261
ER_WARN_TOO_MANY_RECORDS = 1262
ER_WARN_NULL_TO_NOTNULL = 1263
ER_WARN_DATA_OUT_OF_RANGE = 1264
WARN_DATA_TRUNCATED = 1265
ER_WARN_USING_OTHER_HANDLER = 1266
ER_CANT_AGGREGATE_2COLLATIONS = 1267
ER_DROP_USER = 1268
ER_REVOKE_GRANTS = 1269
ER_CANT_AGGREGATE_3COLLATIONS = 1270
ER_CANT_AGGREGATE_NCOLLATIONS = 1271
ER_VARIABLE_IS_NOT_STRUCT = 1272
ER_UNKNOWN_COLLATION = 1273
ER_SLAVE_IGNORED_SSL_PARAMS = 1274
ER_SERVER_IS_IN_SECURE_AUTH_MODE = 1275
ER_WARN_FIELD_RESOLVED = 1276
ER_BAD_SLAVE_UNTIL_COND = 1277
ER_MISSING_SKIP_SLAVE = 1278
ER_UNTIL_COND_IGNORED = 1279
ER_WRONG_NAME_FOR_INDEX = 1280
ER_WRONG_NAME_FOR_CATALOG = 1281
ER_WARN_QC_RESIZE = 1282
ER_BAD_FT_COLUMN = 1283
ER_UNKNOWN_KEY_CACHE = 1284
ER_WARN_HOSTNAME_WONT_WORK = 1285
ER_UNKNOWN_STORAGE_ENGINE = 1286
ER_WARN_DEPRECATED_SYNTAX = 1287
ER_NON_UPDATABLE_TABLE = 1288
ER_FEATURE_DISABLED = 1289
ER_OPTION_PREVENTS_STATEMENT = 1290
ER_DUPLICATED_VALUE_IN_TYPE = 1291
ER_TRUNCATED_WRONG_VALUE = 1292
ER_TOO_MUCH_AUTO_TIMESTAMP_COLS = 1293
ER_INVALID_ON_UPDATE = 1294
ER_UNSUPPORTED_PS = 1295
ER_GET_ERRMSG = 1296
ER_GET_TEMPORARY_ERRMSG = 1297
ER_UNKNOWN_TIME_ZONE = 1298
ER_WARN_INVALID_TIMESTAMP = 1299
ER_INVALID_CHARACTER_STRING = 1300
ER_WARN_ALLOWED_PACKET_OVERFLOWED = 1301
ER_CONFLICTING_DECLARATIONS = 1302
ER_SP_NO_RECURSIVE_CREATE = 1303
ER_SP_ALREADY_EXISTS = 1304
ER_SP_DOES_NOT_EXIST = 1305
ER_SP_DROP_FAILED = 1306
ER_SP_STORE_FAILED = 1307
ER_SP_LILABEL_MISMATCH = 1308
ER_SP_LABEL_REDEFINE = 1309
ER_SP_LABEL_MISMATCH = 1310
ER_SP_UNINIT_VAR = 1311
ER_SP_BADSELECT = 1312
ER_SP_BADRETURN = 1313
ER_SP_BADSTATEMENT = 1314
ER_UPDATE_LOG_DEPRECATED_IGNORED = 1315
ER_UPDATE_LOG_DEPRECATED_TRANSLATED = 1316
ER_QUERY_INTERRUPTED = 1317
ER_SP_WRONG_NO_OF_ARGS = 1318
ER_SP_COND_MISMATCH = 1319
ER_SP_NORETURN = 1320
ER_SP_NORETURNEND = 1321
ER_SP_BAD_CURSOR_QUERY = 1322
ER_SP_BAD_CURSOR_SELECT = 1323
ER_SP_CURSOR_MISMATCH = 1324
ER_SP_CURSOR_ALREADY_OPEN = 1325
ER_SP_CURSOR_NOT_OPEN = 1326
ER_SP_UNDECLARED_VAR = 1327
ER_SP_WRONG_NO_OF_FETCH_ARGS = 1328
ER_SP_FETCH_NO_DATA = 1329
ER_SP_DUP_PARAM = 1330
ER_SP_DUP_VAR = 1331
ER_SP_DUP_COND = 1332
ER_SP_DUP_CURS = 1333
ER_SP_CANT_ALTER = 1334
ER_SP_SUBSELECT_NYI = 1335
ER_STMT_NOT_ALLOWED_IN_SF_OR_TRG = 1336
ER_SP_VARCOND_AFTER_CURSHNDLR = 1337
ER_SP_CURSOR_AFTER_HANDLER = 1338
ER_SP_CASE_NOT_FOUND = 1339
ER_FPARSER_TOO_BIG_FILE = 1340
ER_FPARSER_BAD_HEADER = 1341
ER_FPARSER_EOF_IN_COMMENT = 1342
ER_FPARSER_ERROR_IN_PARAMETER = 1343
ER_FPARSER_EOF_IN_UNKNOWN_PARAMETER = 1344
ER_VIEW_NO_EXPLAIN = 1345
ER_FRM_UNKNOWN_TYPE = 1346
ER_WRONG_OBJECT = 1347
ER_NONUPDATEABLE_COLUMN = 1348
ER_VIEW_SELECT_DERIVED = 1349
ER_VIEW_SELECT_CLAUSE = 1350
ER_VIEW_SELECT_VARIABLE = 1351
ER_VIEW_SELECT_TMPTABLE = 1352
ER_VIEW_WRONG_LIST = 1353
ER_WARN_VIEW_MERGE = 1354
ER_WARN_VIEW_WITHOUT_KEY = 1355
ER_VIEW_INVALID = 1356
ER_SP_NO_DROP_SP = 1357
ER_SP_GOTO_IN_HNDLR = 1358
ER_TRG_ALREADY_EXISTS = 1359
ER_TRG_DOES_NOT_EXIST = 1360
ER_TRG_ON_VIEW_OR_TEMP_TABLE = 1361
ER_TRG_CANT_CHANGE_ROW = 1362
ER_TRG_NO_SUCH_ROW_IN_TRG = 1363
ER_NO_DEFAULT_FOR_FIELD = 1364
ER_DIVISION_BY_ZERO = 1365
ER_TRUNCATED_WRONG_VALUE_FOR_FIELD = 1366
ER_ILLEGAL_VALUE_FOR_TYPE = 1367
ER_VIEW_NONUPD_CHECK = 1368
ER_VIEW_CHECK_FAILED = 1369
ER_PROCACCESS_DENIED_ERROR = 1370
ER_RELAY_LOG_FAIL = 1371
ER_PASSWD_LENGTH = 1372
ER_UNKNOWN_TARGET_BINLOG = 1373
ER_IO_ERR_LOG_INDEX_READ = 1374
ER_BINLOG_PURGE_PROHIBITED = 1375
ER_FSEEK_FAIL = 1376
ER_BINLOG_PURGE_FATAL_ERR = 1377
ER_LOG_IN_USE = 1378
ER_LOG_PURGE_UNKNOWN_ERR = 1379
ER_RELAY_LOG_INIT = 1380
ER_NO_BINARY_LOGGING = 1381
ER_RESERVED_SYNTAX = 1382
ER_WSAS_FAILED = 1383
ER_DIFF_GROUPS_PROC = 1384
ER_NO_GROUP_FOR_PROC = 1385
ER_ORDER_WITH_PROC = 1386
ER_LOGGING_PROHIBIT_CHANGING_OF = 1387
ER_NO_FILE_MAPPING = 1388
ER_WRONG_MAGIC = 1389
ER_PS_MANY_PARAM = 1390
ER_KEY_PART_0 = 1391
ER_VIEW_CHECKSUM = 1392
ER_VIEW_MULTIUPDATE = 1393
ER_VIEW_NO_INSERT_FIELD_LIST = 1394
ER_VIEW_DELETE_MERGE_VIEW = 1395
ER_CANNOT_USER = 1396
ER_XAER_NOTA = 1397
ER_XAER_INVAL = 1398
ER_XAER_RMFAIL = 1399
ER_XAER_OUTSIDE = 1400
ER_XAER_RMERR = 1401
ER_XA_RBROLLBACK = 1402
ER_NONEXISTING_PROC_GRANT = 1403
ER_PROC_AUTO_GRANT_FAIL = 1404
ER_PROC_AUTO_REVOKE_FAIL = 1405
ER_DATA_TOO_LONG = 1406
ER_SP_BAD_SQLSTATE = 1407
ER_STARTUP = 1408
ER_LOAD_FROM_FIXED_SIZE_ROWS_TO_VAR = 1409
ER_CANT_CREATE_USER_WITH_GRANT = 1410
ER_WRONG_VALUE_FOR_TYPE = 1411
ER_TABLE_DEF_CHANGED = 1412
ER_SP_DUP_HANDLER = 1413
ER_SP_NOT_VAR_ARG = 1414
ER_SP_NO_RETSET = 1415
ER_CANT_CREATE_GEOMETRY_OBJECT = 1416
ER_FAILED_ROUTINE_BREAK_BINLOG = 1417
ER_BINLOG_UNSAFE_ROUTINE = 1418
ER_BINLOG_CREATE_ROUTINE_NEED_SUPER = 1419
ER_EXEC_STMT_WITH_OPEN_CURSOR = 1420
ER_STMT_HAS_NO_OPEN_CURSOR = 1421
ER_COMMIT_NOT_ALLOWED_IN_SF_OR_TRG = 1422
ER_NO_DEFAULT_FOR_VIEW_FIELD = 1423
ER_SP_NO_RECURSION = 1424
ER_TOO_BIG_SCALE = 1425
ER_TOO_BIG_PRECISION = 1426
ER_M_BIGGER_THAN_D = 1427
ER_WRONG_LOCK_OF_SYSTEM_TABLE = 1428
ER_CONNECT_TO_FOREIGN_DATA_SOURCE = 1429
ER_QUERY_ON_FOREIGN_DATA_SOURCE = 1430
ER_FOREIGN_DATA_SOURCE_DOESNT_EXIST = 1431
ER_FOREIGN_DATA_STRING_INVALID_CANT_CREATE = 1432
ER_FOREIGN_DATA_STRING_INVALID = 1433
ER_CANT_CREATE_FEDERATED_TABLE = 1434
ER_TRG_IN_WRONG_SCHEMA = 1435
ER_STACK_OVERRUN_NEED_MORE = 1436
ER_TOO_LONG_BODY = 1437
ER_WARN_CANT_DROP_DEFAULT_KEYCACHE = 1438
ER_TOO_BIG_DISPLAYWIDTH = 1439
ER_XAER_DUPID = 1440
ER_DATETIME_FUNCTION_OVERFLOW = 1441
ER_CANT_UPDATE_USED_TABLE_IN_SF_OR_TRG = 1442
ER_VIEW_PREVENT_UPDATE = 1443
ER_PS_NO_RECURSION = 1444
ER_SP_CANT_SET_AUTOCOMMIT = 1445
ER_MALFORMED_DEFINER = 1446
ER_VIEW_FRM_NO_USER = 1447
ER_VIEW_OTHER_USER = 1448
ER_NO_SUCH_USER = 1449
ER_FORBID_SCHEMA_CHANGE = 1450
ER_ROW_IS_REFERENCED_2 = 1451
ER_NO_REFERENCED_ROW_2 = 1452
ER_SP_BAD_VAR_SHADOW = 1453
ER_TRG_NO_DEFINER = 1454
ER_OLD_FILE_FORMAT = 1455
ER_SP_RECURSION_LIMIT = 1456
ER_SP_PROC_TABLE_CORRUPT = 1457
ER_SP_WRONG_NAME = 1458
ER_TABLE_NEEDS_UPGRADE = 1459
ER_SP_NO_AGGREGATE = 1460
ER_MAX_PREPARED_STMT_COUNT_REACHED = 1461
ER_VIEW_RECURSIVE = 1462
ER_NON_GROUPING_FIELD_USED = 1463
ER_TABLE_CANT_HANDLE_SPKEYS = 1464
ER_NO_TRIGGERS_ON_SYSTEM_SCHEMA = 1465
ER_REMOVED_SPACES = 1466
ER_AUTOINC_READ_FAILED = 1467
ER_USERNAME = 1468
ER_HOSTNAME = 1469
ER_WRONG_STRING_LENGTH = 1470
ER_NON_INSERTABLE_TABLE = 1471
ER_ADMIN_WRONG_MRG_TABLE = 1472
ER_TOO_HIGH_LEVEL_OF_NESTING_FOR_SELECT = 1473
ER_NAME_BECOMES_EMPTY = 1474
ER_AMBIGUOUS_FIELD_TERM = 1475
ER_FOREIGN_SERVER_EXISTS = 1476
ER_FOREIGN_SERVER_DOESNT_EXIST = 1477
ER_ILLEGAL_HA_CREATE_OPTION = 1478
ER_PARTITION_REQUIRES_VALUES_ERROR = 1479
ER_PARTITION_WRONG_VALUES_ERROR = 1480
ER_PARTITION_MAXVALUE_ERROR = 1481
ER_PARTITION_SUBPARTITION_ERROR = 1482
ER_PARTITION_SUBPART_MIX_ERROR = 1483
ER_PARTITION_WRONG_NO_PART_ERROR = 1484
ER_PARTITION_WRONG_NO_SUBPART_ERROR = 1485
ER_WRONG_EXPR_IN_PARTITION_FUNC_ERROR = 1486
ER_NO_CONST_EXPR_IN_RANGE_OR_LIST_ERROR = 1487
ER_FIELD_NOT_FOUND_PART_ERROR = 1488
ER_LIST_OF_FIELDS_ONLY_IN_HASH_ERROR = 1489
ER_INCONSISTENT_PARTITION_INFO_ERROR = 1490
ER_PARTITION_FUNC_NOT_ALLOWED_ERROR = 1491
ER_PARTITIONS_MUST_BE_DEFINED_ERROR = 1492
ER_RANGE_NOT_INCREASING_ERROR = 1493
ER_INCONSISTENT_TYPE_OF_FUNCTIONS_ERROR = 1494
ER_MULTIPLE_DEF_CONST_IN_LIST_PART_ERROR = 1495
ER_PARTITION_ENTRY_ERROR = 1496
ER_MIX_HANDLER_ERROR = 1497
ER_PARTITION_NOT_DEFINED_ERROR = 1498
ER_TOO_MANY_PARTITIONS_ERROR = 1499
ER_SUBPARTITION_ERROR = 1500
ER_CANT_CREATE_HANDLER_FILE = 1501
ER_BLOB_FIELD_IN_PART_FUNC_ERROR = 1502
ER_UNIQUE_KEY_NEED_ALL_FIELDS_IN_PF = 1503
ER_NO_PARTS_ERROR = 1504
ER_PARTITION_MGMT_ON_NONPARTITIONED = 1505
ER_FOREIGN_KEY_ON_PARTITIONED = 1506
ER_DROP_PARTITION_NON_EXISTENT = 1507
ER_DROP_LAST_PARTITION = 1508
ER_COALESCE_ONLY_ON_HASH_PARTITION = 1509
ER_REORG_HASH_ONLY_ON_SAME_NO = 1510
ER_REORG_NO_PARAM_ERROR = 1511
ER_ONLY_ON_RANGE_LIST_PARTITION = 1512
ER_ADD_PARTITION_SUBPART_ERROR = 1513
ER_ADD_PARTITION_NO_NEW_PARTITION = 1514
ER_COALESCE_PARTITION_NO_PARTITION = 1515
ER_REORG_PARTITION_NOT_EXIST = 1516
ER_SAME_NAME_PARTITION = 1517
ER_NO_BINLOG_ERROR = 1518
ER_CONSECUTIVE_REORG_PARTITIONS = 1519
ER_REORG_OUTSIDE_RANGE = 1520
ER_PARTITION_FUNCTION_FAILURE = 1521
ER_PART_STATE_ERROR = 1522
ER_LIMITED_PART_RANGE = 1523
ER_PLUGIN_IS_NOT_LOADED = 1524
ER_WRONG_VALUE = 1525
ER_NO_PARTITION_FOR_GIVEN_VALUE = 1526
ER_FILEGROUP_OPTION_ONLY_ONCE = 1527
ER_CREATE_FILEGROUP_FAILED = 1528
ER_DROP_FILEGROUP_FAILED = 1529
ER_TABLESPACE_AUTO_EXTEND_ERROR = 1530
ER_WRONG_SIZE_NUMBER = 1531
ER_SIZE_OVERFLOW_ERROR = 1532
ER_ALTER_FILEGROUP_FAILED = 1533
ER_BINLOG_ROW_LOGGING_FAILED = 1534
ER_BINLOG_ROW_WRONG_TABLE_DEF = 1535
ER_BINLOG_ROW_RBR_TO_SBR = 1536
ER_EVENT_ALREADY_EXISTS = 1537
ER_EVENT_STORE_FAILED = 1538
ER_EVENT_DOES_NOT_EXIST = 1539
ER_EVENT_CANT_ALTER = 1540
ER_EVENT_DROP_FAILED = 1541
ER_EVENT_INTERVAL_NOT_POSITIVE_OR_TOO_BIG = 1542
ER_EVENT_ENDS_BEFORE_STARTS = 1543
ER_EVENT_EXEC_TIME_IN_THE_PAST = 1544
ER_EVENT_OPEN_TABLE_FAILED = 1545
ER_EVENT_NEITHER_M_EXPR_NOR_M_AT = 1546
ER_OBSOLETE_COL_COUNT_DOESNT_MATCH_CORRUPTED = 1547
ER_OBSOLETE_CANNOT_LOAD_FROM_TABLE = 1548
ER_EVENT_CANNOT_DELETE = 1549
ER_EVENT_COMPILE_ERROR = 1550
ER_EVENT_SAME_NAME = 1551
ER_EVENT_DATA_TOO_LONG = 1552
ER_DROP_INDEX_FK = 1553
ER_WARN_DEPRECATED_SYNTAX_WITH_VER = 1554
ER_CANT_WRITE_LOCK_LOG_TABLE = 1555
ER_CANT_LOCK_LOG_TABLE = 1556
ER_FOREIGN_DUPLICATE_KEY_OLD_UNUSED = 1557
ER_COL_COUNT_DOESNT_MATCH_PLEASE_UPDATE = 1558
ER_TEMP_TABLE_PREVENTS_SWITCH_OUT_OF_RBR = 1559
ER_STORED_FUNCTION_PREVENTS_SWITCH_BINLOG_FORMAT = 1560
ER_NDB_CANT_SWITCH_BINLOG_FORMAT = 1561
ER_PARTITION_NO_TEMPORARY = 1562
ER_PARTITION_CONST_DOMAIN_ERROR = 1563
ER_PARTITION_FUNCTION_IS_NOT_ALLOWED = 1564
ER_DDL_LOG_ERROR = 1565
ER_NULL_IN_VALUES_LESS_THAN = 1566
ER_WRONG_PARTITION_NAME = 1567
ER_CANT_CHANGE_TX_CHARACTERISTICS = 1568
ER_DUP_ENTRY_AUTOINCREMENT_CASE = 1569
ER_EVENT_MODIFY_QUEUE_ERROR = 1570
ER_EVENT_SET_VAR_ERROR = 1571
ER_PARTITION_MERGE_ERROR = 1572
ER_CANT_ACTIVATE_LOG = 1573
ER_RBR_NOT_AVAILABLE = 1574
ER_BASE64_DECODE_ERROR = 1575
ER_EVENT_RECURSION_FORBIDDEN = 1576
ER_EVENTS_DB_ERROR = 1577
ER_ONLY_INTEGERS_ALLOWED = 1578
ER_UNSUPORTED_LOG_ENGINE = 1579
ER_BAD_LOG_STATEMENT = 1580
ER_CANT_RENAME_LOG_TABLE = 1581
ER_WRONG_PARAMCOUNT_TO_NATIVE_FCT = 1582
ER_WRONG_PARAMETERS_TO_NATIVE_FCT = 1583
ER_WRONG_PARAMETERS_TO_STORED_FCT = 1584
ER_NATIVE_FCT_NAME_COLLISION = 1585
ER_DUP_ENTRY_WITH_KEY_NAME = 1586
ER_BINLOG_PURGE_EMFILE = 1587
ER_EVENT_CANNOT_CREATE_IN_THE_PAST = 1588
ER_EVENT_CANNOT_ALTER_IN_THE_PAST = 1589
ER_SLAVE_INCIDENT = 1590
ER_NO_PARTITION_FOR_GIVEN_VALUE_SILENT = 1591
ER_BINLOG_UNSAFE_STATEMENT = 1592
ER_SLAVE_FATAL_ERROR = 1593
ER_SLAVE_RELAY_LOG_READ_FAILURE = 1594
ER_SLAVE_RELAY_LOG_WRITE_FAILURE = 1595
ER_SLAVE_CREATE_EVENT_FAILURE = 1596
ER_SLAVE_MASTER_COM_FAILURE = 1597
ER_BINLOG_LOGGING_IMPOSSIBLE = 1598
ER_VIEW_NO_CREATION_CTX = 1599
ER_VIEW_INVALID_CREATION_CTX = 1600
ER_SR_INVALID_CREATION_CTX = 1601
ER_TRG_CORRUPTED_FILE = 1602
ER_TRG_NO_CREATION_CTX = 1603
ER_TRG_INVALID_CREATION_CTX = 1604
ER_EVENT_INVALID_CREATION_CTX = 1605
ER_TRG_CANT_OPEN_TABLE = 1606
ER_CANT_CREATE_SROUTINE = 1607
ER_NEVER_USED = 1608
ER_NO_FORMAT_DESCRIPTION_EVENT_BEFORE_BINLOG_STATEMENT = 1609
ER_SLAVE_CORRUPT_EVENT = 1610
ER_LOAD_DATA_INVALID_COLUMN = 1611
ER_LOG_PURGE_NO_FILE = 1612
ER_XA_RBTIMEOUT = 1613
ER_XA_RBDEADLOCK = 1614
ER_NEED_REPREPARE = 1615
ER_DELAYED_NOT_SUPPORTED = 1616
WARN_NO_MASTER_INFO = 1617
WARN_OPTION_IGNORED = 1618
WARN_PLUGIN_DELETE_BUILTIN = 1619
WARN_PLUGIN_BUSY = 1620
ER_VARIABLE_IS_READONLY = 1621
ER_WARN_ENGINE_TRANSACTION_ROLLBACK = 1622
ER_SLAVE_HEARTBEAT_FAILURE = 1623
ER_SLAVE_HEARTBEAT_VALUE_OUT_OF_RANGE = 1624
ER_NDB_REPLICATION_SCHEMA_ERROR = 1625
ER_CONFLICT_FN_PARSE_ERROR = 1626
ER_EXCEPTIONS_WRITE_ERROR = 1627
ER_TOO_LONG_TABLE_COMMENT = 1628
ER_TOO_LONG_FIELD_COMMENT = 1629
ER_FUNC_INEXISTENT_NAME_COLLISION = 1630
ER_DATABASE_NAME = 1631
ER_TABLE_NAME = 1632
ER_PARTITION_NAME = 1633
ER_SUBPARTITION_NAME = 1634
ER_TEMPORARY_NAME = 1635
ER_RENAMED_NAME = 1636
ER_TOO_MANY_CONCURRENT_TRXS = 1637
WARN_NON_ASCII_SEPARATOR_NOT_IMPLEMENTED = 1638
ER_DEBUG_SYNC_TIMEOUT = 1639
ER_DEBUG_SYNC_HIT_LIMIT = 1640
ER_DUP_SIGNAL_SET = 1641
ER_SIGNAL_WARN = 1642
ER_SIGNAL_NOT_FOUND = 1643
ER_SIGNAL_EXCEPTION = 1644
ER_RESIGNAL_WITHOUT_ACTIVE_HANDLER = 1645
ER_SIGNAL_BAD_CONDITION_TYPE = 1646
WARN_COND_ITEM_TRUNCATED = 1647
ER_COND_ITEM_TOO_LONG = 1648
ER_UNKNOWN_LOCALE = 1649
ER_SLAVE_IGNORE_SERVER_IDS = 1650
ER_QUERY_CACHE_DISABLED = 1651
ER_SAME_NAME_PARTITION_FIELD = 1652
ER_PARTITION_COLUMN_LIST_ERROR = 1653
ER_WRONG_TYPE_COLUMN_VALUE_ERROR = 1654
ER_TOO_MANY_PARTITION_FUNC_FIELDS_ERROR = 1655
ER_MAXVALUE_IN_VALUES_IN = 1656
ER_TOO_MANY_VALUES_ERROR = 1657
ER_ROW_SINGLE_PARTITION_FIELD_ERROR = 1658
ER_FIELD_TYPE_NOT_ALLOWED_AS_PARTITION_FIELD = 1659
ER_PARTITION_FIELDS_TOO_LONG = 1660
ER_BINLOG_ROW_ENGINE_AND_STMT_ENGINE = 1661
ER_BINLOG_ROW_MODE_AND_STMT_ENGINE = 1662
ER_BINLOG_UNSAFE_AND_STMT_ENGINE = 1663
ER_BINLOG_ROW_INJECTION_AND_STMT_ENGINE = 1664
ER_BINLOG_STMT_MODE_AND_ROW_ENGINE = 1665
ER_BINLOG_ROW_INJECTION_AND_STMT_MODE = 1666
ER_BINLOG_MULTIPLE_ENGINES_AND_SELF_LOGGING_ENGINE = 1667
ER_BINLOG_UNSAFE_LIMIT = 1668
ER_UNUSED4 = 1669
ER_BINLOG_UNSAFE_SYSTEM_TABLE = 1670
ER_BINLOG_UNSAFE_AUTOINC_COLUMNS = 1671
ER_BINLOG_UNSAFE_UDF = 1672
ER_BINLOG_UNSAFE_SYSTEM_VARIABLE = 1673
ER_BINLOG_UNSAFE_SYSTEM_FUNCTION = 1674
ER_BINLOG_UNSAFE_NONTRANS_AFTER_TRANS = 1675
ER_MESSAGE_AND_STATEMENT = 1676
ER_SLAVE_CONVERSION_FAILED = 1677
ER_SLAVE_CANT_CREATE_CONVERSION = 1678
ER_INSIDE_TRANSACTION_PREVENTS_SWITCH_BINLOG_FORMAT = 1679
ER_PATH_LENGTH = 1680
ER_WARN_DEPRECATED_SYNTAX_NO_REPLACEMENT = 1681
ER_WRONG_NATIVE_TABLE_STRUCTURE = 1682
ER_WRONG_PERFSCHEMA_USAGE = 1683
ER_WARN_I_S_SKIPPED_TABLE = 1684
ER_INSIDE_TRANSACTION_PREVENTS_SWITCH_BINLOG_DIRECT = 1685
ER_STORED_FUNCTION_PREVENTS_SWITCH_BINLOG_DIRECT = 1686
ER_SPATIAL_MUST_HAVE_GEOM_COL = 1687
ER_TOO_LONG_INDEX_COMMENT = 1688
ER_LOCK_ABORTED = 1689
ER_DATA_OUT_OF_RANGE = 1690
ER_WRONG_SPVAR_TYPE_IN_LIMIT = 1691
ER_BINLOG_UNSAFE_MULTIPLE_ENGINES_AND_SELF_LOGGING_ENGINE = 1692
ER_BINLOG_UNSAFE_MIXED_STATEMENT = 1693
ER_INSIDE_TRANSACTION_PREVENTS_SWITCH_SQL_LOG_BIN = 1694
ER_STORED_FUNCTION_PREVENTS_SWITCH_SQL_LOG_BIN = 1695
ER_FAILED_READ_FROM_PAR_FILE = 1696
ER_VALUES_IS_NOT_INT_TYPE_ERROR = 1697
ER_ACCESS_DENIED_NO_PASSWORD_ERROR = 1698
ER_SET_PASSWORD_AUTH_PLUGIN = 1699
ER_GRANT_PLUGIN_USER_EXISTS = 1700
ER_TRUNCATE_ILLEGAL_FK = 1701
ER_PLUGIN_IS_PERMANENT = 1702
ER_SLAVE_HEARTBEAT_VALUE_OUT_OF_RANGE_MIN = 1703
ER_SLAVE_HEARTBEAT_VALUE_OUT_OF_RANGE_MAX = 1704
ER_STMT_CACHE_FULL = 1705
ER_MULTI_UPDATE_KEY_CONFLICT = 1706
ER_TABLE_NEEDS_REBUILD = 1707
WARN_OPTION_BELOW_LIMIT = 1708
ER_INDEX_COLUMN_TOO_LONG = 1709
ER_ERROR_IN_TRIGGER_BODY = 1710
ER_ERROR_IN_UNKNOWN_TRIGGER_BODY = 1711
ER_INDEX_CORRUPT = 1712
ER_UNDO_RECORD_TOO_BIG = 1713
ER_BINLOG_UNSAFE_INSERT_IGNORE_SELECT = 1714
ER_BINLOG_UNSAFE_INSERT_SELECT_UPDATE = 1715
ER_BINLOG_UNSAFE_REPLACE_SELECT = 1716
ER_BINLOG_UNSAFE_CREATE_IGNORE_SELECT = 1717
ER_BINLOG_UNSAFE_CREATE_REPLACE_SELECT = 1718
ER_BINLOG_UNSAFE_UPDATE_IGNORE = 1719
ER_PLUGIN_NO_UNINSTALL = 1720
ER_PLUGIN_NO_INSTALL = 1721
ER_BINLOG_UNSAFE_WRITE_AUTOINC_SELECT = 1722
ER_BINLOG_UNSAFE_CREATE_SELECT_AUTOINC = 1723
ER_BINLOG_UNSAFE_INSERT_TWO_KEYS = 1724
ER_TABLE_IN_FK_CHECK = 1725
ER_UNSUPPORTED_ENGINE = 1726
ER_BINLOG_UNSAFE_AUTOINC_NOT_FIRST = 1727
ER_CANNOT_LOAD_FROM_TABLE_V2 = 1728
ER_MASTER_DELAY_VALUE_OUT_OF_RANGE = 1729
ER_ONLY_FD_AND_RBR_EVENTS_ALLOWED_IN_BINLOG_STATEMENT = 1730
ER_PARTITION_EXCHANGE_DIFFERENT_OPTION = 1731
ER_PARTITION_EXCHANGE_PART_TABLE = 1732
ER_PARTITION_EXCHANGE_TEMP_TABLE = 1733
ER_PARTITION_INSTEAD_OF_SUBPARTITION = 1734
ER_UNKNOWN_PARTITION = 1735
ER_TABLES_DIFFERENT_METADATA = 1736
ER_ROW_DOES_NOT_MATCH_PARTITION = 1737
ER_BINLOG_CACHE_SIZE_GREATER_THAN_MAX = 1738
ER_WARN_INDEX_NOT_APPLICABLE = 1739
ER_PARTITION_EXCHANGE_FOREIGN_KEY = 1740
ER_NO_SUCH_KEY_VALUE = 1741
ER_RPL_INFO_DATA_TOO_LONG = 1742
ER_NETWORK_READ_EVENT_CHECKSUM_FAILURE = 1743
ER_BINLOG_READ_EVENT_CHECKSUM_FAILURE = 1744
ER_BINLOG_STMT_CACHE_SIZE_GREATER_THAN_MAX = 1745
ER_CANT_UPDATE_TABLE_IN_CREATE_TABLE_SELECT = 1746
ER_PARTITION_CLAUSE_ON_NONPARTITIONED = 1747
ER_ROW_DOES_NOT_MATCH_GIVEN_PARTITION_SET = 1748
ER_NO_SUCH_PARTITION__UNUSED = 1749
ER_CHANGE_RPL_INFO_REPOSITORY_FAILURE = 1750
ER_WARNING_NOT_COMPLETE_ROLLBACK_WITH_CREATED_TEMP_TABLE = 1751
ER_WARNING_NOT_COMPLETE_ROLLBACK_WITH_DROPPED_TEMP_TABLE = 1752
ER_MTS_FEATURE_IS_NOT_SUPPORTED = 1753
ER_MTS_UPDATED_DBS_GREATER_MAX = 1754
ER_MTS_CANT_PARALLEL = 1755
ER_MTS_INCONSISTENT_DATA = 1756
ER_FULLTEXT_NOT_SUPPORTED_WITH_PARTITIONING = 1757
ER_DA_INVALID_CONDITION_NUMBER = 1758
ER_INSECURE_PLAIN_TEXT = 1759
ER_INSECURE_CHANGE_MASTER = 1760
ER_FOREIGN_DUPLICATE_KEY_WITH_CHILD_INFO = 1761
ER_FOREIGN_DUPLICATE_KEY_WITHOUT_CHILD_INFO = 1762
ER_SQLTHREAD_WITH_SECURE_SLAVE = 1763
ER_TABLE_HAS_NO_FT = 1764
ER_VARIABLE_NOT_SETTABLE_IN_SF_OR_TRIGGER = 1765
ER_VARIABLE_NOT_SETTABLE_IN_TRANSACTION = 1766
ER_GTID_NEXT_IS_NOT_IN_GTID_NEXT_LIST = 1767
ER_CANT_CHANGE_GTID_NEXT_IN_TRANSACTION_WHEN_GTID_NEXT_LIST_IS_NULL = 1768
ER_SET_STATEMENT_CANNOT_INVOKE_FUNCTION = 1769
ER_GTID_NEXT_CANT_BE_AUTOMATIC_IF_GTID_NEXT_LIST_IS_NON_NULL = 1770
ER_SKIPPING_LOGGED_TRANSACTION = 1771
ER_MALFORMED_GTID_SET_SPECIFICATION = 1772
ER_MALFORMED_GTID_SET_ENCODING = 1773
ER_MALFORMED_GTID_SPECIFICATION = 1774
ER_GNO_EXHAUSTED = 1775
ER_BAD_SLAVE_AUTO_POSITION = 1776
ER_AUTO_POSITION_REQUIRES_GTID_MODE_ON = 1777
ER_CANT_DO_IMPLICIT_COMMIT_IN_TRX_WHEN_GTID_NEXT_IS_SET = 1778
ER_GTID_MODE_2_OR_3_REQUIRES_ENFORCE_GTID_CONSISTENCY_ON = 1779
ER_GTID_MODE_REQUIRES_BINLOG = 1780
ER_CANT_SET_GTID_NEXT_TO_GTID_WHEN_GTID_MODE_IS_OFF = 1781
ER_CANT_SET_GTID_NEXT_TO_ANONYMOUS_WHEN_GTID_MODE_IS_ON = 1782
ER_CANT_SET_GTID_NEXT_LIST_TO_NON_NULL_WHEN_GTID_MODE_IS_OFF = 1783
ER_FOUND_GTID_EVENT_WHEN_GTID_MODE_IS_OFF = 1784
ER_GTID_UNSAFE_NON_TRANSACTIONAL_TABLE = 1785
ER_GTID_UNSAFE_CREATE_SELECT = 1786
ER_GTID_UNSAFE_CREATE_DROP_TEMPORARY_TABLE_IN_TRANSACTION = 1787
ER_GTID_MODE_CAN_ONLY_CHANGE_ONE_STEP_AT_A_TIME = 1788
ER_MASTER_HAS_PURGED_REQUIRED_GTIDS = 1789
ER_CANT_SET_GTID_NEXT_WHEN_OWNING_GTID = 1790
ER_UNKNOWN_EXPLAIN_FORMAT = 1791
ER_CANT_EXECUTE_IN_READ_ONLY_TRANSACTION = 1792
ER_TOO_LONG_TABLE_PARTITION_COMMENT = 1793
ER_SLAVE_CONFIGURATION = 1794
ER_INNODB_FT_LIMIT = 1795
ER_INNODB_NO_FT_TEMP_TABLE = 1796
ER_INNODB_FT_WRONG_DOCID_COLUMN = 1797
ER_INNODB_FT_WRONG_DOCID_INDEX = 1798
ER_INNODB_ONLINE_LOG_TOO_BIG = 1799
ER_UNKNOWN_ALTER_ALGORITHM = 1800
ER_UNKNOWN_ALTER_LOCK = 1801
ER_MTS_CHANGE_MASTER_CANT_RUN_WITH_GAPS = 1802
ER_MTS_RECOVERY_FAILURE = 1803
ER_MTS_RESET_WORKERS = 1804
ER_COL_COUNT_DOESNT_MATCH_CORRUPTED_V2 = 1805
ER_SLAVE_SILENT_RETRY_TRANSACTION = 1806
ER_DISCARD_FK_CHECKS_RUNNING = 1807
ER_TABLE_SCHEMA_MISMATCH = 1808
ER_TABLE_IN_SYSTEM_TABLESPACE = 1809
ER_IO_READ_ERROR = 1810
ER_IO_WRITE_ERROR = 1811
ER_TABLESPACE_MISSING = 1812
ER_TABLESPACE_EXISTS = 1813
ER_TABLESPACE_DISCARDED = 1814
ER_INTERNAL_ERROR = 1815
ER_INNODB_IMPORT_ERROR = 1816
ER_INNODB_INDEX_CORRUPT = 1817
ER_INVALID_YEAR_COLUMN_LENGTH = 1818
ER_NOT_VALID_PASSWORD = 1819
ER_MUST_CHANGE_PASSWORD = 1820
ER_FK_NO_INDEX_CHILD = 1821
ER_FK_NO_INDEX_PARENT = 1822
ER_FK_FAIL_ADD_SYSTEM = 1823
ER_FK_CANNOT_OPEN_PARENT = 1824
ER_FK_INCORRECT_OPTION = 1825
ER_FK_DUP_NAME = 1826
ER_PASSWORD_FORMAT = 1827
ER_FK_COLUMN_CANNOT_DROP = 1828
ER_FK_COLUMN_CANNOT_DROP_CHILD = 1829
ER_FK_COLUMN_NOT_NULL = 1830
ER_DUP_INDEX = 1831
ER_FK_COLUMN_CANNOT_CHANGE = 1832
ER_FK_COLUMN_CANNOT_CHANGE_CHILD = 1833
ER_FK_CANNOT_DELETE_PARENT = 1834
ER_MALFORMED_PACKET = 1835
ER_READ_ONLY_MODE = 1836
ER_GTID_NEXT_TYPE_UNDEFINED_GROUP = 1837
ER_VARIABLE_NOT_SETTABLE_IN_SP = 1838
ER_CANT_SET_GTID_PURGED_WHEN_GTID_MODE_IS_OFF = 1839
ER_CANT_SET_GTID_PURGED_WHEN_GTID_EXECUTED_IS_NOT_EMPTY = 1840
ER_CANT_SET_GTID_PURGED_WHEN_OWNED_GTIDS_IS_NOT_EMPTY = 1841
ER_GTID_PURGED_WAS_CHANGED = 1842
ER_GTID_EXECUTED_WAS_CHANGED = 1843
ER_BINLOG_STMT_MODE_AND_NO_REPL_TABLES = 1844
ER_ALTER_OPERATION_NOT_SUPPORTED = 1845
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON = 1846
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_COPY = 1847
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_PARTITION = 1848
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_FK_RENAME = 1849
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_COLUMN_TYPE = 1850
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_FK_CHECK = 1851
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_IGNORE = 1852
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_NOPK = 1853
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_AUTOINC = 1854
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_HIDDEN_FTS = 1855
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_CHANGE_FTS = 1856
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_FTS = 1857
ER_SQL_SLAVE_SKIP_COUNTER_NOT_SETTABLE_IN_GTID_MODE = 1858
ER_DUP_UNKNOWN_IN_INDEX = 1859
ER_IDENT_CAUSES_TOO_LONG_PATH = 1860
ER_ALTER_OPERATION_NOT_SUPPORTED_REASON_NOT_NULL = 1861
ER_MUST_CHANGE_PASSWORD_LOGIN = 1862
ER_ROW_IN_WRONG_PARTITION = 1863
ER_MTS_EVENT_BIGGER_PENDING_JOBS_SIZE_MAX = 1864
ER_INNODB_NO_FT_USES_PARSER = 1865
ER_BINLOG_LOGICAL_CORRUPTION = 1866
ER_WARN_PURGE_LOG_IN_USE = 1867
ER_WARN_PURGE_LOG_IS_ACTIVE = 1868
ER_AUTO_INCREMENT_CONFLICT = 1869
WARN_ON_BLOCKHOLE_IN_RBR = 1870
ER_SLAVE_MI_INIT_REPOSITORY = 1871
ER_SLAVE_RLI_INIT_REPOSITORY = 1872
ER_ACCESS_DENIED_CHANGE_USER_ERROR = 1873
ER_INNODB_READ_ONLY = 1874
ER_STOP_SLAVE_SQL_THREAD_TIMEOUT = 1875
ER_STOP_SLAVE_IO_THREAD_TIMEOUT = 1876
ER_TABLE_CORRUPT = 1877
ER_FILE_CORRUPT = 1878
ER_ERROR_ON_MASTER = 1879
ER_INCONSISTENT_ERROR = 1880
ER_STORAGE_ENGINE_NOT_LOADED = 1881
ER_GET_STACKED_DA_WITHOUT_ACTIVE_HANDLER = 1882
ER_WARN_LEGACY_SYNTAX_CONVERTED = 1883
ER_BINLOG_UNSAFE_FULLTEXT_PLUGIN = 1884
ER_CANNOT_DISCARD_TEMPORARY_TABLE = 1885
ER_FK_DEPTH_EXCEEDED = 1886
ER_COL_COUNT_DOESNT_MATCH_PLEASE_UPDATE_V2 = 1887
ER_WARN_TRIGGER_DOESNT_HAVE_CREATED = 1888
ER_REFERENCED_TRG_DOES_NOT_EXIST = 1889
ER_EXPLAIN_NOT_SUPPORTED = 1890
ER_INVALID_FIELD_SIZE = 1891
ER_MISSING_HA_CREATE_OPTION = 1892
CR_UNKNOWN_ERROR = 2000
CR_SOCKET_CREATE_ERROR = 2001
CR_CONNECTION_ERROR = 2002
CR_CONN_HOST_ERROR = 2003
CR_IPSOCK_ERROR = 2004
CR_UNKNOWN_HOST = 2005
CR_SERVER_GONE_ERROR = 2006
CR_VERSION_ERROR = 2007
CR_OUT_OF_MEMORY = 2008
CR_WRONG_HOST_INFO = 2009
CR_LOCALHOST_CONNECTION = 2010
CR_TCP_CONNECTION = 2011
CR_SERVER_HANDSHAKE_ERR = 2012
CR_SERVER_LOST = 2013
CR_COMMANDS_OUT_OF_SYNC = 2014
CR_NAMEDPIPE_CONNECTION = 2015
CR_NAMEDPIPEWAIT_ERROR = 2016
CR_NAMEDPIPEOPEN_ERROR = 2017
CR_NAMEDPIPESETSTATE_ERROR = 2018
CR_CANT_READ_CHARSET = 2019
CR_NET_PACKET_TOO_LARGE = 2020
CR_EMBEDDED_CONNECTION = 2021
CR_PROBE_SLAVE_STATUS = 2022
CR_PROBE_SLAVE_HOSTS = 2023
CR_PROBE_SLAVE_CONNECT = 2024
CR_PROBE_MASTER_CONNECT = 2025
CR_SSL_CONNECTION_ERROR = 2026
CR_MALFORMED_PACKET = 2027
CR_WRONG_LICENSE = 2028
CR_NULL_POINTER = 2029
CR_NO_PREPARE_STMT = 2030
CR_PARAMS_NOT_BOUND = 2031
CR_DATA_TRUNCATED = 2032
CR_NO_PARAMETERS_EXISTS = 2033
CR_INVALID_PARAMETER_NO = 2034
CR_INVALID_BUFFER_USE = 2035
CR_UNSUPPORTED_PARAM_TYPE = 2036
CR_SHARED_MEMORY_CONNECTION = 2037
CR_SHARED_MEMORY_CONNECT_REQUEST_ERROR = 2038
CR_SHARED_MEMORY_CONNECT_ANSWER_ERROR = 2039
CR_SHARED_MEMORY_CONNECT_FILE_MAP_ERROR = 2040
CR_SHARED_MEMORY_CONNECT_MAP_ERROR = 2041
CR_SHARED_MEMORY_FILE_MAP_ERROR = 2042
CR_SHARED_MEMORY_MAP_ERROR = 2043
CR_SHARED_MEMORY_EVENT_ERROR = 2044
CR_SHARED_MEMORY_CONNECT_ABANDONED_ERROR = 2045
CR_SHARED_MEMORY_CONNECT_SET_ERROR = 2046
CR_CONN_UNKNOW_PROTOCOL = 2047
CR_INVALID_CONN_HANDLE = 2048
CR_SECURE_AUTH = 2049
CR_FETCH_CANCELED = 2050
CR_NO_DATA = 2051
CR_NO_STMT_METADATA = 2052
CR_NO_RESULT_SET = 2053
CR_NOT_IMPLEMENTED = 2054
CR_SERVER_LOST_EXTENDED = 2055
CR_STMT_CLOSED = 2056
CR_NEW_STMT_METADATA = 2057
CR_ALREADY_CONNECTED = 2058
CR_AUTH_PLUGIN_CANNOT_LOAD = 2059
CR_DUPLICATE_CONNECTION_ATTR = 2060
CR_AUTH_PLUGIN_ERR = 2061
# End MySQL Errors

