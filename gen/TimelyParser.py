# Generated from C:/Users/PARSA/Desktop/elmos/Semesters/S7/Compiler/Programs/compiler-project/grammar/Timely.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,486,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,1,4,1,73,8,1,11,1,12,1,74,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,83,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,204,8,8,1,8,1,8,1,
        8,1,8,1,8,3,8,211,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,235,8,8,1,8,1,
        8,1,8,1,8,3,8,241,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,269,8,8,1,8,1,8,1,8,1,8,3,8,275,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,307,8,8,1,8,1,8,1,8,1,8,3,8,313,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,359,8,8,
        1,8,1,8,1,8,1,8,1,8,3,8,366,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,390,
        8,8,1,8,1,8,1,8,1,8,3,8,396,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,3,8,424,8,8,1,8,1,8,1,8,1,8,3,8,430,8,8,3,8,432,8,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,
        15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,
        21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,
        28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,0,
        0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,0,3,1,0,43,47,2,0,35,35,48,52,
        1,0,53,54,477,0,68,1,0,0,0,2,72,1,0,0,0,4,82,1,0,0,0,6,84,1,0,0,
        0,8,113,1,0,0,0,10,150,1,0,0,0,12,163,1,0,0,0,14,176,1,0,0,0,16,
        431,1,0,0,0,18,433,1,0,0,0,20,436,1,0,0,0,22,439,1,0,0,0,24,441,
        1,0,0,0,26,443,1,0,0,0,28,445,1,0,0,0,30,447,1,0,0,0,32,449,1,0,
        0,0,34,451,1,0,0,0,36,453,1,0,0,0,38,455,1,0,0,0,40,457,1,0,0,0,
        42,459,1,0,0,0,44,461,1,0,0,0,46,463,1,0,0,0,48,465,1,0,0,0,50,467,
        1,0,0,0,52,469,1,0,0,0,54,471,1,0,0,0,56,473,1,0,0,0,58,475,1,0,
        0,0,60,477,1,0,0,0,62,479,1,0,0,0,64,481,1,0,0,0,66,483,1,0,0,0,
        68,69,3,2,1,0,69,70,5,0,0,1,70,1,1,0,0,0,71,73,3,4,2,0,72,71,1,0,
        0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,3,1,0,0,0,76,83,
        3,6,3,0,77,83,3,8,4,0,78,83,3,10,5,0,79,83,3,12,6,0,80,83,3,14,7,
        0,81,83,3,16,8,0,82,76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,
        1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,5,1,0,0,0,84,85,3,36,18,0,
        85,86,5,1,0,0,86,87,5,2,0,0,87,88,5,3,0,0,88,89,5,4,0,0,89,90,3,
        24,12,0,90,91,5,5,0,0,91,92,5,6,0,0,92,93,5,1,0,0,93,94,3,32,16,
        0,94,95,5,5,0,0,95,96,5,7,0,0,96,97,5,1,0,0,97,98,3,34,17,0,98,99,
        5,5,0,0,99,100,5,8,0,0,100,101,5,1,0,0,101,102,3,38,19,0,102,103,
        5,5,0,0,103,104,5,9,0,0,104,105,5,1,0,0,105,106,3,40,20,0,106,107,
        5,5,0,0,107,108,5,10,0,0,108,109,5,1,0,0,109,110,3,42,21,0,110,111,
        1,0,0,0,111,112,5,11,0,0,112,7,1,0,0,0,113,114,3,36,18,0,114,115,
        5,1,0,0,115,116,5,2,0,0,116,117,5,3,0,0,117,118,5,12,0,0,118,119,
        3,26,13,0,119,120,5,5,0,0,120,121,5,13,0,0,121,122,5,1,0,0,122,123,
        3,46,23,0,123,124,5,5,0,0,124,125,5,14,0,0,125,126,5,1,0,0,126,127,
        3,48,24,0,127,128,5,5,0,0,128,129,5,15,0,0,129,130,5,1,0,0,130,131,
        3,50,25,0,131,132,5,5,0,0,132,133,5,7,0,0,133,134,5,1,0,0,134,135,
        3,22,11,0,135,136,5,5,0,0,136,137,5,8,0,0,137,138,5,1,0,0,138,139,
        3,38,19,0,139,140,5,5,0,0,140,141,5,9,0,0,141,142,5,1,0,0,142,143,
        3,40,20,0,143,144,5,5,0,0,144,145,5,10,0,0,145,146,5,1,0,0,146,147,
        3,42,21,0,147,148,1,0,0,0,148,149,5,11,0,0,149,9,1,0,0,0,150,151,
        5,16,0,0,151,152,5,4,0,0,152,153,5,1,0,0,153,154,3,36,18,0,154,155,
        5,5,0,0,155,156,5,17,0,0,156,157,5,1,0,0,157,158,3,52,26,0,158,159,
        5,5,0,0,159,160,5,18,0,0,160,161,5,1,0,0,161,162,3,54,27,0,162,11,
        1,0,0,0,163,164,5,19,0,0,164,165,5,4,0,0,165,166,5,1,0,0,166,167,
        3,36,18,0,167,168,5,5,0,0,168,169,5,17,0,0,169,170,5,1,0,0,170,171,
        3,52,26,0,171,172,5,5,0,0,172,173,5,18,0,0,173,174,5,1,0,0,174,175,
        3,54,27,0,175,13,1,0,0,0,176,177,5,20,0,0,177,178,5,21,0,0,178,179,
        3,36,18,0,179,15,1,0,0,0,180,181,5,22,0,0,181,182,5,23,0,0,182,183,
        5,24,0,0,183,184,5,25,0,0,184,185,5,1,0,0,185,186,3,56,28,0,186,
        187,5,26,0,0,187,188,3,36,18,0,188,189,5,5,0,0,189,190,5,27,0,0,
        190,191,5,1,0,0,191,192,3,44,22,0,192,193,1,0,0,0,193,194,5,5,0,
        0,194,195,5,10,0,0,195,196,5,1,0,0,196,197,3,42,21,0,197,203,1,0,
        0,0,198,199,5,5,0,0,199,200,3,18,9,0,200,201,5,28,0,0,201,202,3,
        28,14,0,202,204,1,0,0,0,203,198,1,0,0,0,203,204,1,0,0,0,204,210,
        1,0,0,0,205,206,5,5,0,0,206,207,3,20,10,0,207,208,5,28,0,0,208,209,
        3,30,15,0,209,211,1,0,0,0,210,205,1,0,0,0,210,211,1,0,0,0,211,432,
        1,0,0,0,212,213,5,22,0,0,213,214,5,29,0,0,214,215,5,24,0,0,215,216,
        5,30,0,0,216,217,5,1,0,0,217,218,3,58,29,0,218,219,5,26,0,0,219,
        220,3,36,18,0,220,221,5,5,0,0,221,222,5,27,0,0,222,223,5,1,0,0,223,
        224,3,44,22,0,224,225,1,0,0,0,225,226,5,5,0,0,226,227,5,10,0,0,227,
        228,5,1,0,0,228,229,3,42,21,0,229,234,1,0,0,0,230,231,5,5,0,0,231,
        232,5,31,0,0,232,233,5,28,0,0,233,235,3,28,14,0,234,230,1,0,0,0,
        234,235,1,0,0,0,235,240,1,0,0,0,236,237,5,5,0,0,237,238,5,32,0,0,
        238,239,5,28,0,0,239,241,3,30,15,0,240,236,1,0,0,0,240,241,1,0,0,
        0,241,432,1,0,0,0,242,243,5,22,0,0,243,244,5,33,0,0,244,245,5,24,
        0,0,245,246,5,25,0,0,246,247,5,1,0,0,247,248,3,56,28,0,248,249,5,
        5,0,0,249,250,5,30,0,0,250,251,5,1,0,0,251,252,3,58,29,0,252,253,
        5,26,0,0,253,254,3,36,18,0,254,255,5,5,0,0,255,256,5,27,0,0,256,
        257,5,1,0,0,257,258,3,44,22,0,258,259,1,0,0,0,259,260,5,5,0,0,260,
        261,5,10,0,0,261,262,5,1,0,0,262,263,3,42,21,0,263,268,1,0,0,0,264,
        265,5,5,0,0,265,266,5,31,0,0,266,267,5,28,0,0,267,269,3,28,14,0,
        268,264,1,0,0,0,268,269,1,0,0,0,269,274,1,0,0,0,270,271,5,5,0,0,
        271,272,5,32,0,0,272,273,5,28,0,0,273,275,3,30,15,0,274,270,1,0,
        0,0,274,275,1,0,0,0,275,432,1,0,0,0,276,277,5,22,0,0,277,278,5,34,
        0,0,278,279,5,24,0,0,279,280,5,25,0,0,280,281,5,1,0,0,281,282,3,
        56,28,0,282,283,5,5,0,0,283,284,5,30,0,0,284,285,5,1,0,0,285,286,
        3,58,29,0,286,287,5,5,0,0,287,288,5,35,0,0,288,289,5,1,0,0,289,290,
        3,60,30,0,290,291,5,26,0,0,291,292,3,36,18,0,292,293,5,5,0,0,293,
        294,5,27,0,0,294,295,5,1,0,0,295,296,3,44,22,0,296,297,1,0,0,0,297,
        298,5,5,0,0,298,299,5,10,0,0,299,300,5,1,0,0,300,301,3,42,21,0,301,
        306,1,0,0,0,302,303,5,5,0,0,303,304,5,31,0,0,304,305,5,28,0,0,305,
        307,3,28,14,0,306,302,1,0,0,0,306,307,1,0,0,0,307,312,1,0,0,0,308,
        309,5,5,0,0,309,310,5,32,0,0,310,311,5,28,0,0,311,313,3,30,15,0,
        312,308,1,0,0,0,312,313,1,0,0,0,313,432,1,0,0,0,314,315,5,22,0,0,
        315,316,5,36,0,0,316,317,5,24,0,0,317,318,5,25,0,0,318,319,5,1,0,
        0,319,320,3,56,28,0,320,321,5,5,0,0,321,322,5,30,0,0,322,323,5,1,
        0,0,323,324,3,58,29,0,324,325,5,5,0,0,325,326,5,35,0,0,326,327,5,
        1,0,0,327,328,3,60,30,0,328,329,5,26,0,0,329,330,5,24,0,0,330,331,
        5,37,0,0,331,332,5,1,0,0,332,333,3,62,31,0,333,334,5,5,0,0,334,335,
        5,38,0,0,335,336,5,1,0,0,336,337,3,64,32,0,337,338,5,5,0,0,338,339,
        5,39,0,0,339,340,5,1,0,0,340,341,3,66,33,0,341,342,5,26,0,0,342,
        343,3,36,18,0,343,344,5,5,0,0,344,345,5,27,0,0,345,346,5,1,0,0,346,
        347,3,44,22,0,347,348,1,0,0,0,348,349,5,5,0,0,349,350,5,10,0,0,350,
        351,5,1,0,0,351,352,3,42,21,0,352,358,1,0,0,0,353,354,5,5,0,0,354,
        355,3,18,9,0,355,356,5,28,0,0,356,357,3,28,14,0,357,359,1,0,0,0,
        358,353,1,0,0,0,358,359,1,0,0,0,359,365,1,0,0,0,360,361,5,5,0,0,
        361,362,3,20,10,0,362,363,5,28,0,0,363,364,3,30,15,0,364,366,1,0,
        0,0,365,360,1,0,0,0,365,366,1,0,0,0,366,432,1,0,0,0,367,368,5,22,
        0,0,368,369,5,40,0,0,369,370,5,24,0,0,370,371,5,25,0,0,371,372,5,
        1,0,0,372,373,3,56,28,0,373,374,5,26,0,0,374,375,3,36,18,0,375,376,
        5,5,0,0,376,377,5,27,0,0,377,378,5,1,0,0,378,379,3,44,22,0,379,380,
        1,0,0,0,380,381,5,5,0,0,381,382,5,10,0,0,382,383,5,1,0,0,383,384,
        3,42,21,0,384,389,1,0,0,0,385,386,5,5,0,0,386,387,5,31,0,0,387,388,
        5,28,0,0,388,390,3,28,14,0,389,385,1,0,0,0,389,390,1,0,0,0,390,395,
        1,0,0,0,391,392,5,5,0,0,392,393,5,32,0,0,393,394,5,28,0,0,394,396,
        3,30,15,0,395,391,1,0,0,0,395,396,1,0,0,0,396,432,1,0,0,0,397,398,
        5,22,0,0,398,399,5,41,0,0,399,400,5,24,0,0,400,401,5,25,0,0,401,
        402,5,1,0,0,402,403,3,56,28,0,403,404,5,5,0,0,404,405,5,30,0,0,405,
        406,5,1,0,0,406,407,3,58,29,0,407,408,5,26,0,0,408,409,3,36,18,0,
        409,410,5,5,0,0,410,411,5,27,0,0,411,412,5,1,0,0,412,413,3,44,22,
        0,413,414,1,0,0,0,414,415,5,5,0,0,415,416,5,10,0,0,416,417,5,1,0,
        0,417,418,3,42,21,0,418,423,1,0,0,0,419,420,5,5,0,0,420,421,5,31,
        0,0,421,422,5,28,0,0,422,424,3,28,14,0,423,419,1,0,0,0,423,424,1,
        0,0,0,424,429,1,0,0,0,425,426,5,5,0,0,426,427,5,32,0,0,427,428,5,
        28,0,0,428,430,3,30,15,0,429,425,1,0,0,0,429,430,1,0,0,0,430,432,
        1,0,0,0,431,180,1,0,0,0,431,212,1,0,0,0,431,242,1,0,0,0,431,276,
        1,0,0,0,431,314,1,0,0,0,431,367,1,0,0,0,431,397,1,0,0,0,432,17,1,
        0,0,0,433,434,5,31,0,0,434,435,5,22,0,0,435,19,1,0,0,0,436,437,5,
        31,0,0,437,438,5,42,0,0,438,21,1,0,0,0,439,440,7,0,0,0,440,23,1,
        0,0,0,441,442,5,58,0,0,442,25,1,0,0,0,443,444,5,58,0,0,444,27,1,
        0,0,0,445,446,5,59,0,0,446,29,1,0,0,0,447,448,5,59,0,0,448,31,1,
        0,0,0,449,450,5,59,0,0,450,33,1,0,0,0,451,452,5,59,0,0,452,35,1,
        0,0,0,453,454,5,58,0,0,454,37,1,0,0,0,455,456,5,55,0,0,456,39,1,
        0,0,0,457,458,5,55,0,0,458,41,1,0,0,0,459,460,5,57,0,0,460,43,1,
        0,0,0,461,462,5,57,0,0,462,45,1,0,0,0,463,464,7,1,0,0,464,47,1,0,
        0,0,465,466,5,55,0,0,466,49,1,0,0,0,467,468,5,55,0,0,468,51,1,0,
        0,0,469,470,5,56,0,0,470,53,1,0,0,0,471,472,7,2,0,0,472,55,1,0,0,
        0,473,474,5,56,0,0,474,57,1,0,0,0,475,476,5,56,0,0,476,59,1,0,0,
        0,477,478,5,56,0,0,478,61,1,0,0,0,479,480,5,56,0,0,480,63,1,0,0,
        0,481,482,5,56,0,0,482,65,1,0,0,0,483,484,5,56,0,0,484,67,1,0,0,
        0,17,74,82,203,210,234,240,268,274,306,312,358,365,389,395,423,429,
        431
    ]

class TimelyParser ( Parser ):

    grammarFileName = "Timely.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'{'", "'load'", "'data'", "','", 
                     "'time'", "'value'", "'trainEnd'", "'testEnd'", "'visualize'", 
                     "'}'", "'ticker'", "'interval'", "'start'", "'end'", 
                     "'acf'", "'lags'", "'type'", "'pacf'", "'test'", "'adf'", 
                     "'model'", "'AR'", "'('", "'p'", "')'", "'summary'", 
                     "'as'", "'MA'", "'q'", "'save'", "'save_chart'", "'ARMA'", 
                     "'ARIMA'", "'d'", "'SARIMA'", "'P'", "'Q'", "'D'", 
                     "'ARCH'", "'GARCH'", "'chart'", "'Open'", "'High'", 
                     "'Low'", "'Close'", "'Adj Close'", "'s'", "'m'", "'h'", 
                     "'M'", "'y'", "'Plot'", "'Bar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DATE", "INT", 
                      "BOOL", "ID", "STRING", "WS", "COMMENT" ]

    RULE_start = 0
    RULE_program = 1
    RULE_statement = 2
    RULE_dataframeLoadStatement = 3
    RULE_tickerLoadStatement = 4
    RULE_acfStatement = 5
    RULE_pacfStatement = 6
    RULE_testStatement = 7
    RULE_modelStatement = 8
    RULE_save_model = 9
    RULE_save_chart = 10
    RULE_price_value = 11
    RULE_csv_address = 12
    RULE_ticker_name = 13
    RULE_model_name = 14
    RULE_chart_name = 15
    RULE_time = 16
    RULE_value = 17
    RULE_dataframe_name = 18
    RULE_train_end = 19
    RULE_test_end = 20
    RULE_visualize = 21
    RULE_summary = 22
    RULE_interval = 23
    RULE_start_time = 24
    RULE_end_time = 25
    RULE_lags = 26
    RULE_type = 27
    RULE_p = 28
    RULE_q = 29
    RULE_d = 30
    RULE_ps = 31
    RULE_qs = 32
    RULE_ds = 33

    ruleNames =  [ "start", "program", "statement", "dataframeLoadStatement", 
                   "tickerLoadStatement", "acfStatement", "pacfStatement", 
                   "testStatement", "modelStatement", "save_model", "save_chart", 
                   "price_value", "csv_address", "ticker_name", "model_name", 
                   "chart_name", "time", "value", "dataframe_name", "train_end", 
                   "test_end", "visualize", "summary", "interval", "start_time", 
                   "end_time", "lags", "type", "p", "q", "d", "ps", "qs", 
                   "ds" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    DATE=55
    INT=56
    BOOL=57
    ID=58
    STRING=59
    WS=60
    COMMENT=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(TimelyParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(TimelyParser.EOF, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = TimelyParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.program()
            self.state = 69
            self.match(TimelyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TimelyParser.StatementContext)
            else:
                return self.getTypedRuleContext(TimelyParser.StatementContext,i)


        def getRuleIndex(self):
            return TimelyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TimelyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.statement()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 288230376157544448) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataframeLoadStatement(self):
            return self.getTypedRuleContext(TimelyParser.DataframeLoadStatementContext,0)


        def tickerLoadStatement(self):
            return self.getTypedRuleContext(TimelyParser.TickerLoadStatementContext,0)


        def acfStatement(self):
            return self.getTypedRuleContext(TimelyParser.AcfStatementContext,0)


        def pacfStatement(self):
            return self.getTypedRuleContext(TimelyParser.PacfStatementContext,0)


        def testStatement(self):
            return self.getTypedRuleContext(TimelyParser.TestStatementContext,0)


        def modelStatement(self):
            return self.getTypedRuleContext(TimelyParser.ModelStatementContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TimelyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.dataframeLoadStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.tickerLoadStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.acfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.pacfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.testStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.modelStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataframeLoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


        def csv_address(self):
            return self.getTypedRuleContext(TimelyParser.Csv_addressContext,0)


        def time(self):
            return self.getTypedRuleContext(TimelyParser.TimeContext,0)


        def value(self):
            return self.getTypedRuleContext(TimelyParser.ValueContext,0)


        def train_end(self):
            return self.getTypedRuleContext(TimelyParser.Train_endContext,0)


        def test_end(self):
            return self.getTypedRuleContext(TimelyParser.Test_endContext,0)


        def visualize(self):
            return self.getTypedRuleContext(TimelyParser.VisualizeContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_dataframeLoadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataframeLoadStatement" ):
                listener.enterDataframeLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataframeLoadStatement" ):
                listener.exitDataframeLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataframeLoadStatement" ):
                return visitor.visitDataframeLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def dataframeLoadStatement(self):

        localctx = TimelyParser.DataframeLoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dataframeLoadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.dataframe_name()
            self.state = 85
            self.match(TimelyParser.T__0)
            self.state = 86
            self.match(TimelyParser.T__1)
            self.state = 87
            self.match(TimelyParser.T__2)
            self.state = 88
            self.match(TimelyParser.T__3)
            self.state = 89
            self.csv_address()
            self.state = 90
            self.match(TimelyParser.T__4)
            self.state = 91
            self.match(TimelyParser.T__5)
            self.state = 92
            self.match(TimelyParser.T__0)
            self.state = 93
            self.time()
            self.state = 94
            self.match(TimelyParser.T__4)
            self.state = 95
            self.match(TimelyParser.T__6)
            self.state = 96
            self.match(TimelyParser.T__0)
            self.state = 97
            self.value()
            self.state = 98
            self.match(TimelyParser.T__4)
            self.state = 99
            self.match(TimelyParser.T__7)
            self.state = 100
            self.match(TimelyParser.T__0)
            self.state = 101
            self.train_end()
            self.state = 102
            self.match(TimelyParser.T__4)
            self.state = 103
            self.match(TimelyParser.T__8)
            self.state = 104
            self.match(TimelyParser.T__0)
            self.state = 105
            self.test_end()

            self.state = 106
            self.match(TimelyParser.T__4)
            self.state = 107
            self.match(TimelyParser.T__9)
            self.state = 108
            self.match(TimelyParser.T__0)
            self.state = 109
            self.visualize()
            self.state = 111
            self.match(TimelyParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TickerLoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


        def ticker_name(self):
            return self.getTypedRuleContext(TimelyParser.Ticker_nameContext,0)


        def interval(self):
            return self.getTypedRuleContext(TimelyParser.IntervalContext,0)


        def start_time(self):
            return self.getTypedRuleContext(TimelyParser.Start_timeContext,0)


        def end_time(self):
            return self.getTypedRuleContext(TimelyParser.End_timeContext,0)


        def price_value(self):
            return self.getTypedRuleContext(TimelyParser.Price_valueContext,0)


        def train_end(self):
            return self.getTypedRuleContext(TimelyParser.Train_endContext,0)


        def test_end(self):
            return self.getTypedRuleContext(TimelyParser.Test_endContext,0)


        def visualize(self):
            return self.getTypedRuleContext(TimelyParser.VisualizeContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_tickerLoadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTickerLoadStatement" ):
                listener.enterTickerLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTickerLoadStatement" ):
                listener.exitTickerLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTickerLoadStatement" ):
                return visitor.visitTickerLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def tickerLoadStatement(self):

        localctx = TimelyParser.TickerLoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tickerLoadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.dataframe_name()
            self.state = 114
            self.match(TimelyParser.T__0)
            self.state = 115
            self.match(TimelyParser.T__1)
            self.state = 116
            self.match(TimelyParser.T__2)
            self.state = 117
            self.match(TimelyParser.T__11)
            self.state = 118
            self.ticker_name()
            self.state = 119
            self.match(TimelyParser.T__4)
            self.state = 120
            self.match(TimelyParser.T__12)
            self.state = 121
            self.match(TimelyParser.T__0)
            self.state = 122
            self.interval()
            self.state = 123
            self.match(TimelyParser.T__4)
            self.state = 124
            self.match(TimelyParser.T__13)
            self.state = 125
            self.match(TimelyParser.T__0)
            self.state = 126
            self.start_time()
            self.state = 127
            self.match(TimelyParser.T__4)
            self.state = 128
            self.match(TimelyParser.T__14)
            self.state = 129
            self.match(TimelyParser.T__0)
            self.state = 130
            self.end_time()
            self.state = 131
            self.match(TimelyParser.T__4)
            self.state = 132
            self.match(TimelyParser.T__6)
            self.state = 133
            self.match(TimelyParser.T__0)
            self.state = 134
            self.price_value()
            self.state = 135
            self.match(TimelyParser.T__4)
            self.state = 136
            self.match(TimelyParser.T__7)
            self.state = 137
            self.match(TimelyParser.T__0)
            self.state = 138
            self.train_end()
            self.state = 139
            self.match(TimelyParser.T__4)
            self.state = 140
            self.match(TimelyParser.T__8)
            self.state = 141
            self.match(TimelyParser.T__0)
            self.state = 142
            self.test_end()

            self.state = 143
            self.match(TimelyParser.T__4)
            self.state = 144
            self.match(TimelyParser.T__9)
            self.state = 145
            self.match(TimelyParser.T__0)
            self.state = 146
            self.visualize()
            self.state = 148
            self.match(TimelyParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


        def lags(self):
            return self.getTypedRuleContext(TimelyParser.LagsContext,0)


        def type_(self):
            return self.getTypedRuleContext(TimelyParser.TypeContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_acfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcfStatement" ):
                listener.enterAcfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcfStatement" ):
                listener.exitAcfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcfStatement" ):
                return visitor.visitAcfStatement(self)
            else:
                return visitor.visitChildren(self)




    def acfStatement(self):

        localctx = TimelyParser.AcfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_acfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(TimelyParser.T__15)
            self.state = 151
            self.match(TimelyParser.T__3)
            self.state = 152
            self.match(TimelyParser.T__0)
            self.state = 153
            self.dataframe_name()
            self.state = 154
            self.match(TimelyParser.T__4)
            self.state = 155
            self.match(TimelyParser.T__16)
            self.state = 156
            self.match(TimelyParser.T__0)
            self.state = 157
            self.lags()
            self.state = 158
            self.match(TimelyParser.T__4)
            self.state = 159
            self.match(TimelyParser.T__17)
            self.state = 160
            self.match(TimelyParser.T__0)
            self.state = 161
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PacfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


        def lags(self):
            return self.getTypedRuleContext(TimelyParser.LagsContext,0)


        def type_(self):
            return self.getTypedRuleContext(TimelyParser.TypeContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_pacfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPacfStatement" ):
                listener.enterPacfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPacfStatement" ):
                listener.exitPacfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPacfStatement" ):
                return visitor.visitPacfStatement(self)
            else:
                return visitor.visitChildren(self)




    def pacfStatement(self):

        localctx = TimelyParser.PacfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pacfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(TimelyParser.T__18)
            self.state = 164
            self.match(TimelyParser.T__3)
            self.state = 165
            self.match(TimelyParser.T__0)
            self.state = 166
            self.dataframe_name()
            self.state = 167
            self.match(TimelyParser.T__4)
            self.state = 168
            self.match(TimelyParser.T__16)
            self.state = 169
            self.match(TimelyParser.T__0)
            self.state = 170
            self.lags()
            self.state = 171
            self.match(TimelyParser.T__4)
            self.state = 172
            self.match(TimelyParser.T__17)
            self.state = 173
            self.match(TimelyParser.T__0)
            self.state = 174
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_testStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestStatement" ):
                listener.enterTestStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestStatement" ):
                listener.exitTestStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestStatement" ):
                return visitor.visitTestStatement(self)
            else:
                return visitor.visitChildren(self)




    def testStatement(self):

        localctx = TimelyParser.TestStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_testStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(TimelyParser.T__19)
            self.state = 177
            self.match(TimelyParser.T__20)
            self.state = 178
            self.dataframe_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p(self):
            return self.getTypedRuleContext(TimelyParser.PContext,0)


        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


        def summary(self):
            return self.getTypedRuleContext(TimelyParser.SummaryContext,0)


        def visualize(self):
            return self.getTypedRuleContext(TimelyParser.VisualizeContext,0)


        def save_model(self):
            return self.getTypedRuleContext(TimelyParser.Save_modelContext,0)


        def model_name(self):
            return self.getTypedRuleContext(TimelyParser.Model_nameContext,0)


        def save_chart(self):
            return self.getTypedRuleContext(TimelyParser.Save_chartContext,0)


        def chart_name(self):
            return self.getTypedRuleContext(TimelyParser.Chart_nameContext,0)


        def q(self):
            return self.getTypedRuleContext(TimelyParser.QContext,0)


        def d(self):
            return self.getTypedRuleContext(TimelyParser.DContext,0)


        def ps(self):
            return self.getTypedRuleContext(TimelyParser.PsContext,0)


        def qs(self):
            return self.getTypedRuleContext(TimelyParser.QsContext,0)


        def ds(self):
            return self.getTypedRuleContext(TimelyParser.DsContext,0)


        def getRuleIndex(self):
            return TimelyParser.RULE_modelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelStatement" ):
                listener.enterModelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelStatement" ):
                listener.exitModelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelStatement" ):
                return visitor.visitModelStatement(self)
            else:
                return visitor.visitChildren(self)




    def modelStatement(self):

        localctx = TimelyParser.ModelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_modelStatement)
        self._la = 0 # Token type
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(TimelyParser.T__21)
                self.state = 181
                self.match(TimelyParser.T__22)
                self.state = 182
                self.match(TimelyParser.T__23)
                self.state = 183
                self.match(TimelyParser.T__24)
                self.state = 184
                self.match(TimelyParser.T__0)
                self.state = 185
                self.p()
                self.state = 186
                self.match(TimelyParser.T__25)
                self.state = 187
                self.dataframe_name()

                self.state = 188
                self.match(TimelyParser.T__4)
                self.state = 189
                self.match(TimelyParser.T__26)
                self.state = 190
                self.match(TimelyParser.T__0)
                self.state = 191
                self.summary()

                self.state = 193
                self.match(TimelyParser.T__4)
                self.state = 194
                self.match(TimelyParser.T__9)
                self.state = 195
                self.match(TimelyParser.T__0)
                self.state = 196
                self.visualize()
                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 198
                    self.match(TimelyParser.T__4)
                    self.state = 199
                    self.save_model()
                    self.state = 200
                    self.match(TimelyParser.T__27)
                    self.state = 201
                    self.model_name()


                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 205
                    self.match(TimelyParser.T__4)
                    self.state = 206
                    self.save_chart()
                    self.state = 207
                    self.match(TimelyParser.T__27)
                    self.state = 208
                    self.chart_name()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(TimelyParser.T__21)
                self.state = 213
                self.match(TimelyParser.T__28)
                self.state = 214
                self.match(TimelyParser.T__23)
                self.state = 215
                self.match(TimelyParser.T__29)
                self.state = 216
                self.match(TimelyParser.T__0)
                self.state = 217
                self.q()
                self.state = 218
                self.match(TimelyParser.T__25)
                self.state = 219
                self.dataframe_name()

                self.state = 220
                self.match(TimelyParser.T__4)
                self.state = 221
                self.match(TimelyParser.T__26)
                self.state = 222
                self.match(TimelyParser.T__0)
                self.state = 223
                self.summary()

                self.state = 225
                self.match(TimelyParser.T__4)
                self.state = 226
                self.match(TimelyParser.T__9)
                self.state = 227
                self.match(TimelyParser.T__0)
                self.state = 228
                self.visualize()
                self.state = 234
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 230
                    self.match(TimelyParser.T__4)
                    self.state = 231
                    self.match(TimelyParser.T__30)
                    self.state = 232
                    self.match(TimelyParser.T__27)
                    self.state = 233
                    self.model_name()


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 236
                    self.match(TimelyParser.T__4)
                    self.state = 237
                    self.match(TimelyParser.T__31)
                    self.state = 238
                    self.match(TimelyParser.T__27)
                    self.state = 239
                    self.chart_name()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(TimelyParser.T__21)
                self.state = 243
                self.match(TimelyParser.T__32)
                self.state = 244
                self.match(TimelyParser.T__23)
                self.state = 245
                self.match(TimelyParser.T__24)
                self.state = 246
                self.match(TimelyParser.T__0)
                self.state = 247
                self.p()
                self.state = 248
                self.match(TimelyParser.T__4)
                self.state = 249
                self.match(TimelyParser.T__29)
                self.state = 250
                self.match(TimelyParser.T__0)
                self.state = 251
                self.q()
                self.state = 252
                self.match(TimelyParser.T__25)
                self.state = 253
                self.dataframe_name()

                self.state = 254
                self.match(TimelyParser.T__4)
                self.state = 255
                self.match(TimelyParser.T__26)
                self.state = 256
                self.match(TimelyParser.T__0)
                self.state = 257
                self.summary()

                self.state = 259
                self.match(TimelyParser.T__4)
                self.state = 260
                self.match(TimelyParser.T__9)
                self.state = 261
                self.match(TimelyParser.T__0)
                self.state = 262
                self.visualize()
                self.state = 268
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 264
                    self.match(TimelyParser.T__4)
                    self.state = 265
                    self.match(TimelyParser.T__30)
                    self.state = 266
                    self.match(TimelyParser.T__27)
                    self.state = 267
                    self.model_name()


                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 270
                    self.match(TimelyParser.T__4)
                    self.state = 271
                    self.match(TimelyParser.T__31)
                    self.state = 272
                    self.match(TimelyParser.T__27)
                    self.state = 273
                    self.chart_name()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 276
                self.match(TimelyParser.T__21)
                self.state = 277
                self.match(TimelyParser.T__33)
                self.state = 278
                self.match(TimelyParser.T__23)
                self.state = 279
                self.match(TimelyParser.T__24)
                self.state = 280
                self.match(TimelyParser.T__0)
                self.state = 281
                self.p()
                self.state = 282
                self.match(TimelyParser.T__4)
                self.state = 283
                self.match(TimelyParser.T__29)
                self.state = 284
                self.match(TimelyParser.T__0)
                self.state = 285
                self.q()
                self.state = 286
                self.match(TimelyParser.T__4)
                self.state = 287
                self.match(TimelyParser.T__34)
                self.state = 288
                self.match(TimelyParser.T__0)
                self.state = 289
                self.d()
                self.state = 290
                self.match(TimelyParser.T__25)
                self.state = 291
                self.dataframe_name()

                self.state = 292
                self.match(TimelyParser.T__4)
                self.state = 293
                self.match(TimelyParser.T__26)
                self.state = 294
                self.match(TimelyParser.T__0)
                self.state = 295
                self.summary()

                self.state = 297
                self.match(TimelyParser.T__4)
                self.state = 298
                self.match(TimelyParser.T__9)
                self.state = 299
                self.match(TimelyParser.T__0)
                self.state = 300
                self.visualize()
                self.state = 306
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 302
                    self.match(TimelyParser.T__4)
                    self.state = 303
                    self.match(TimelyParser.T__30)
                    self.state = 304
                    self.match(TimelyParser.T__27)
                    self.state = 305
                    self.model_name()


                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 308
                    self.match(TimelyParser.T__4)
                    self.state = 309
                    self.match(TimelyParser.T__31)
                    self.state = 310
                    self.match(TimelyParser.T__27)
                    self.state = 311
                    self.chart_name()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.match(TimelyParser.T__21)
                self.state = 315
                self.match(TimelyParser.T__35)
                self.state = 316
                self.match(TimelyParser.T__23)
                self.state = 317
                self.match(TimelyParser.T__24)
                self.state = 318
                self.match(TimelyParser.T__0)
                self.state = 319
                self.p()
                self.state = 320
                self.match(TimelyParser.T__4)
                self.state = 321
                self.match(TimelyParser.T__29)
                self.state = 322
                self.match(TimelyParser.T__0)
                self.state = 323
                self.q()
                self.state = 324
                self.match(TimelyParser.T__4)
                self.state = 325
                self.match(TimelyParser.T__34)
                self.state = 326
                self.match(TimelyParser.T__0)
                self.state = 327
                self.d()
                self.state = 328
                self.match(TimelyParser.T__25)
                self.state = 329
                self.match(TimelyParser.T__23)
                self.state = 330
                self.match(TimelyParser.T__36)
                self.state = 331
                self.match(TimelyParser.T__0)
                self.state = 332
                self.ps()
                self.state = 333
                self.match(TimelyParser.T__4)
                self.state = 334
                self.match(TimelyParser.T__37)
                self.state = 335
                self.match(TimelyParser.T__0)
                self.state = 336
                self.qs()
                self.state = 337
                self.match(TimelyParser.T__4)
                self.state = 338
                self.match(TimelyParser.T__38)
                self.state = 339
                self.match(TimelyParser.T__0)
                self.state = 340
                self.ds()
                self.state = 341
                self.match(TimelyParser.T__25)
                self.state = 342
                self.dataframe_name()

                self.state = 343
                self.match(TimelyParser.T__4)
                self.state = 344
                self.match(TimelyParser.T__26)
                self.state = 345
                self.match(TimelyParser.T__0)
                self.state = 346
                self.summary()

                self.state = 348
                self.match(TimelyParser.T__4)
                self.state = 349
                self.match(TimelyParser.T__9)
                self.state = 350
                self.match(TimelyParser.T__0)
                self.state = 351
                self.visualize()
                self.state = 358
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 353
                    self.match(TimelyParser.T__4)
                    self.state = 354
                    self.save_model()
                    self.state = 355
                    self.match(TimelyParser.T__27)
                    self.state = 356
                    self.model_name()


                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 360
                    self.match(TimelyParser.T__4)
                    self.state = 361
                    self.save_chart()
                    self.state = 362
                    self.match(TimelyParser.T__27)
                    self.state = 363
                    self.chart_name()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 367
                self.match(TimelyParser.T__21)
                self.state = 368
                self.match(TimelyParser.T__39)
                self.state = 369
                self.match(TimelyParser.T__23)
                self.state = 370
                self.match(TimelyParser.T__24)
                self.state = 371
                self.match(TimelyParser.T__0)
                self.state = 372
                self.p()
                self.state = 373
                self.match(TimelyParser.T__25)
                self.state = 374
                self.dataframe_name()

                self.state = 375
                self.match(TimelyParser.T__4)
                self.state = 376
                self.match(TimelyParser.T__26)
                self.state = 377
                self.match(TimelyParser.T__0)
                self.state = 378
                self.summary()

                self.state = 380
                self.match(TimelyParser.T__4)
                self.state = 381
                self.match(TimelyParser.T__9)
                self.state = 382
                self.match(TimelyParser.T__0)
                self.state = 383
                self.visualize()
                self.state = 389
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 385
                    self.match(TimelyParser.T__4)
                    self.state = 386
                    self.match(TimelyParser.T__30)
                    self.state = 387
                    self.match(TimelyParser.T__27)
                    self.state = 388
                    self.model_name()


                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 391
                    self.match(TimelyParser.T__4)
                    self.state = 392
                    self.match(TimelyParser.T__31)
                    self.state = 393
                    self.match(TimelyParser.T__27)
                    self.state = 394
                    self.chart_name()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 397
                self.match(TimelyParser.T__21)
                self.state = 398
                self.match(TimelyParser.T__40)
                self.state = 399
                self.match(TimelyParser.T__23)
                self.state = 400
                self.match(TimelyParser.T__24)
                self.state = 401
                self.match(TimelyParser.T__0)
                self.state = 402
                self.p()
                self.state = 403
                self.match(TimelyParser.T__4)
                self.state = 404
                self.match(TimelyParser.T__29)
                self.state = 405
                self.match(TimelyParser.T__0)
                self.state = 406
                self.q()
                self.state = 407
                self.match(TimelyParser.T__25)
                self.state = 408
                self.dataframe_name()

                self.state = 409
                self.match(TimelyParser.T__4)
                self.state = 410
                self.match(TimelyParser.T__26)
                self.state = 411
                self.match(TimelyParser.T__0)
                self.state = 412
                self.summary()

                self.state = 414
                self.match(TimelyParser.T__4)
                self.state = 415
                self.match(TimelyParser.T__9)
                self.state = 416
                self.match(TimelyParser.T__0)
                self.state = 417
                self.visualize()
                self.state = 423
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 419
                    self.match(TimelyParser.T__4)
                    self.state = 420
                    self.match(TimelyParser.T__30)
                    self.state = 421
                    self.match(TimelyParser.T__27)
                    self.state = 422
                    self.model_name()


                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 425
                    self.match(TimelyParser.T__4)
                    self.state = 426
                    self.match(TimelyParser.T__31)
                    self.state = 427
                    self.match(TimelyParser.T__27)
                    self.state = 428
                    self.chart_name()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Save_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TimelyParser.RULE_save_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSave_model" ):
                listener.enterSave_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSave_model" ):
                listener.exitSave_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSave_model" ):
                return visitor.visitSave_model(self)
            else:
                return visitor.visitChildren(self)




    def save_model(self):

        localctx = TimelyParser.Save_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_save_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(TimelyParser.T__30)
            self.state = 434
            self.match(TimelyParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Save_chartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TimelyParser.RULE_save_chart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSave_chart" ):
                listener.enterSave_chart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSave_chart" ):
                listener.exitSave_chart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSave_chart" ):
                return visitor.visitSave_chart(self)
            else:
                return visitor.visitChildren(self)




    def save_chart(self):

        localctx = TimelyParser.Save_chartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_save_chart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(TimelyParser.T__30)
            self.state = 437
            self.match(TimelyParser.T__41)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Price_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TimelyParser.RULE_price_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrice_value" ):
                listener.enterPrice_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrice_value" ):
                listener.exitPrice_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrice_value" ):
                return visitor.visitPrice_value(self)
            else:
                return visitor.visitChildren(self)




    def price_value(self):

        localctx = TimelyParser.Price_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_price_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 272678883688448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Csv_addressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TimelyParser.ID, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_csv_address

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsv_address" ):
                listener.enterCsv_address(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsv_address" ):
                listener.exitCsv_address(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCsv_address" ):
                return visitor.visitCsv_address(self)
            else:
                return visitor.visitChildren(self)




    def csv_address(self):

        localctx = TimelyParser.Csv_addressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_csv_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(TimelyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ticker_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TimelyParser.ID, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_ticker_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTicker_name" ):
                listener.enterTicker_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTicker_name" ):
                listener.exitTicker_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTicker_name" ):
                return visitor.visitTicker_name(self)
            else:
                return visitor.visitChildren(self)




    def ticker_name(self):

        localctx = TimelyParser.Ticker_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ticker_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(TimelyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_model_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_name" ):
                listener.enterModel_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_name" ):
                listener.exitModel_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel_name" ):
                return visitor.visitModel_name(self)
            else:
                return visitor.visitChildren(self)




    def model_name(self):

        localctx = TimelyParser.Model_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_model_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chart_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_chart_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChart_name" ):
                listener.enterChart_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChart_name" ):
                listener.exitChart_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChart_name" ):
                return visitor.visitChart_name(self)
            else:
                return visitor.visitChildren(self)




    def chart_name(self):

        localctx = TimelyParser.Chart_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_chart_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime" ):
                return visitor.visitTime(self)
            else:
                return visitor.visitChildren(self)




    def time(self):

        localctx = TimelyParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = TimelyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dataframe_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TimelyParser.ID, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_dataframe_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataframe_name" ):
                listener.enterDataframe_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataframe_name" ):
                listener.exitDataframe_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataframe_name" ):
                return visitor.visitDataframe_name(self)
            else:
                return visitor.visitChildren(self)




    def dataframe_name(self):

        localctx = TimelyParser.Dataframe_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dataframe_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(TimelyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Train_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(TimelyParser.DATE, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_train_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrain_end" ):
                listener.enterTrain_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrain_end" ):
                listener.exitTrain_end(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrain_end" ):
                return visitor.visitTrain_end(self)
            else:
                return visitor.visitChildren(self)




    def train_end(self):

        localctx = TimelyParser.Train_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_train_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(TimelyParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(TimelyParser.DATE, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_test_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest_end" ):
                listener.enterTest_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest_end" ):
                listener.exitTest_end(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest_end" ):
                return visitor.visitTest_end(self)
            else:
                return visitor.visitChildren(self)




    def test_end(self):

        localctx = TimelyParser.Test_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_test_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(TimelyParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(TimelyParser.BOOL, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_visualize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualize" ):
                listener.enterVisualize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualize" ):
                listener.exitVisualize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualize" ):
                return visitor.visitVisualize(self)
            else:
                return visitor.visitChildren(self)




    def visualize(self):

        localctx = TimelyParser.VisualizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_visualize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(TimelyParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(TimelyParser.BOOL, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_summary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummary" ):
                listener.enterSummary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummary" ):
                listener.exitSummary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummary" ):
                return visitor.visitSummary(self)
            else:
                return visitor.visitChildren(self)




    def summary(self):

        localctx = TimelyParser.SummaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(TimelyParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TimelyParser.RULE_interval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterval" ):
                listener.enterInterval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterval" ):
                listener.exitInterval(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterval" ):
                return visitor.visitInterval(self)
            else:
                return visitor.visitChildren(self)




    def interval(self):

        localctx = TimelyParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_interval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8725758637768704) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(TimelyParser.DATE, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_start_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_time" ):
                listener.enterStart_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_time" ):
                listener.exitStart_time(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_time" ):
                return visitor.visitStart_time(self)
            else:
                return visitor.visitChildren(self)




    def start_time(self):

        localctx = TimelyParser.Start_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_start_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(TimelyParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(TimelyParser.DATE, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_end_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_time" ):
                listener.enterEnd_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_time" ):
                listener.exitEnd_time(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_time" ):
                return visitor.visitEnd_time(self)
            else:
                return visitor.visitChildren(self)




    def end_time(self):

        localctx = TimelyParser.End_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_end_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(TimelyParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_lags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLags" ):
                listener.enterLags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLags" ):
                listener.exitLags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLags" ):
                return visitor.visitLags(self)
            else:
                return visitor.visitChildren(self)




    def lags(self):

        localctx = TimelyParser.LagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TimelyParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = TimelyParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not(_la==53 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP" ):
                listener.enterP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP" ):
                listener.exitP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP" ):
                return visitor.visitP(self)
            else:
                return visitor.visitChildren(self)




    def p(self):

        localctx = TimelyParser.PContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_q

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQ" ):
                listener.enterQ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQ" ):
                listener.exitQ(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQ" ):
                return visitor.visitQ(self)
            else:
                return visitor.visitChildren(self)




    def q(self):

        localctx = TimelyParser.QContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_q)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD" ):
                listener.enterD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD" ):
                listener.exitD(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD" ):
                return visitor.visitD(self)
            else:
                return visitor.visitChildren(self)




    def d(self):

        localctx = TimelyParser.DContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_ps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPs" ):
                listener.enterPs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPs" ):
                listener.exitPs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPs" ):
                return visitor.visitPs(self)
            else:
                return visitor.visitChildren(self)




    def ps(self):

        localctx = TimelyParser.PsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ps)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_qs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQs" ):
                listener.enterQs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQs" ):
                listener.exitQs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQs" ):
                return visitor.visitQs(self)
            else:
                return visitor.visitChildren(self)




    def qs(self):

        localctx = TimelyParser.QsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_qs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_ds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDs" ):
                listener.enterDs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDs" ):
                listener.exitDs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDs" ):
                return visitor.visitDs(self)
            else:
                return visitor.visitChildren(self)




    def ds(self):

        localctx = TimelyParser.DsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





