# Generated from D:/Compiler/project/compiler-project/grammar/Timely.g4 by ANTLR 4.13.1
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
        4,1,65,620,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,1,4,1,111,8,1,11,1,12,1,112,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,121,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,148,8,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,183,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,223,8,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,236,8,9,1,9,1,9,3,9,240,8,9,1,
        9,1,9,1,9,1,9,1,9,3,9,247,8,9,1,9,1,9,1,9,1,9,1,9,3,9,254,8,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,267,8,
        10,1,10,1,10,3,10,271,8,10,1,10,1,10,1,10,1,10,1,10,3,10,278,8,10,
        1,10,1,10,1,10,1,10,1,10,3,10,285,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,302,8,11,
        1,11,1,11,3,11,306,8,11,1,11,1,11,1,11,1,11,1,11,3,11,313,8,11,1,
        11,1,11,1,11,1,11,1,11,3,11,320,8,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,341,8,12,1,12,1,12,3,12,345,8,12,1,12,1,12,1,12,1,12,1,12,
        3,12,352,8,12,1,12,1,12,1,12,1,12,1,12,3,12,359,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,397,8,13,1,13,1,13,3,
        13,401,8,13,1,13,1,13,1,13,1,13,1,13,3,13,408,8,13,1,13,1,13,1,13,
        1,13,1,13,3,13,415,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,3,14,428,8,14,1,14,1,14,3,14,432,8,14,1,14,1,14,1,
        14,1,14,1,14,3,14,439,8,14,1,14,1,14,1,14,1,14,1,14,3,14,446,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,3,15,463,8,15,1,15,1,15,3,15,467,8,15,1,15,1,15,1,15,1,
        15,1,15,3,15,474,8,15,1,15,1,15,1,15,1,15,1,15,3,15,481,8,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,526,8,16,1,16,1,16,3,16,530,8,16,1,16,1,16,1,
        16,1,16,1,16,3,16,537,8,16,1,16,1,16,1,16,1,16,1,16,3,16,544,8,16,
        1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,
        1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,
        1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,
        1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,
        1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,
        1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,52,0,0,53,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,
        96,98,100,102,104,0,2,1,0,50,54,1,0,56,57,613,0,106,1,0,0,0,2,110,
        1,0,0,0,4,120,1,0,0,0,6,122,1,0,0,0,8,149,1,0,0,0,10,184,1,0,0,0,
        12,197,1,0,0,0,14,210,1,0,0,0,16,222,1,0,0,0,18,224,1,0,0,0,20,255,
        1,0,0,0,22,286,1,0,0,0,24,321,1,0,0,0,26,360,1,0,0,0,28,416,1,0,
        0,0,30,447,1,0,0,0,32,482,1,0,0,0,34,545,1,0,0,0,36,548,1,0,0,0,
        38,551,1,0,0,0,40,553,1,0,0,0,42,555,1,0,0,0,44,557,1,0,0,0,46,559,
        1,0,0,0,48,561,1,0,0,0,50,563,1,0,0,0,52,565,1,0,0,0,54,567,1,0,
        0,0,56,569,1,0,0,0,58,571,1,0,0,0,60,573,1,0,0,0,62,575,1,0,0,0,
        64,577,1,0,0,0,66,579,1,0,0,0,68,581,1,0,0,0,70,583,1,0,0,0,72,585,
        1,0,0,0,74,587,1,0,0,0,76,589,1,0,0,0,78,591,1,0,0,0,80,593,1,0,
        0,0,82,595,1,0,0,0,84,597,1,0,0,0,86,599,1,0,0,0,88,601,1,0,0,0,
        90,603,1,0,0,0,92,605,1,0,0,0,94,607,1,0,0,0,96,609,1,0,0,0,98,611,
        1,0,0,0,100,613,1,0,0,0,102,615,1,0,0,0,104,617,1,0,0,0,106,107,
        3,2,1,0,107,108,5,0,0,1,108,1,1,0,0,0,109,111,3,4,2,0,110,109,1,
        0,0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,3,1,0,
        0,0,114,121,3,6,3,0,115,121,3,8,4,0,116,121,3,10,5,0,117,121,3,12,
        6,0,118,121,3,14,7,0,119,121,3,16,8,0,120,114,1,0,0,0,120,115,1,
        0,0,0,120,116,1,0,0,0,120,117,1,0,0,0,120,118,1,0,0,0,120,119,1,
        0,0,0,121,5,1,0,0,0,122,123,5,1,0,0,123,124,5,2,0,0,124,125,3,54,
        27,0,125,126,5,3,0,0,126,127,3,54,27,0,127,128,5,4,0,0,128,129,5,
        5,0,0,129,130,5,6,0,0,130,131,3,50,25,0,131,132,5,4,0,0,132,133,
        5,7,0,0,133,134,5,6,0,0,134,135,3,52,26,0,135,136,5,4,0,0,136,137,
        5,8,0,0,137,138,5,6,0,0,138,139,3,56,28,0,139,140,5,4,0,0,140,141,
        5,9,0,0,141,142,5,6,0,0,142,147,3,58,29,0,143,144,5,4,0,0,144,145,
        5,10,0,0,145,146,5,6,0,0,146,148,3,64,32,0,147,143,1,0,0,0,147,148,
        1,0,0,0,148,7,1,0,0,0,149,150,5,1,0,0,150,151,5,11,0,0,151,152,3,
        40,20,0,152,153,5,3,0,0,153,154,3,54,27,0,154,155,5,4,0,0,155,156,
        5,12,0,0,156,157,5,6,0,0,157,158,3,66,33,0,158,159,5,4,0,0,159,160,
        5,13,0,0,160,161,5,6,0,0,161,162,3,68,34,0,162,163,5,4,0,0,163,164,
        5,14,0,0,164,165,5,6,0,0,165,166,3,70,35,0,166,167,5,4,0,0,167,168,
        5,7,0,0,168,169,5,6,0,0,169,170,3,38,19,0,170,171,5,4,0,0,171,172,
        5,8,0,0,172,173,5,6,0,0,173,174,3,56,28,0,174,175,5,4,0,0,175,176,
        5,9,0,0,176,177,5,6,0,0,177,182,3,58,29,0,178,179,5,4,0,0,179,180,
        5,10,0,0,180,181,5,6,0,0,181,183,3,64,32,0,182,178,1,0,0,0,182,183,
        1,0,0,0,183,9,1,0,0,0,184,185,5,15,0,0,185,186,5,2,0,0,186,187,5,
        6,0,0,187,188,3,54,27,0,188,189,5,4,0,0,189,190,5,16,0,0,190,191,
        5,6,0,0,191,192,3,72,36,0,192,193,5,4,0,0,193,194,5,17,0,0,194,195,
        5,6,0,0,195,196,3,74,37,0,196,11,1,0,0,0,197,198,5,18,0,0,198,199,
        5,2,0,0,199,200,5,6,0,0,200,201,3,54,27,0,201,202,5,4,0,0,202,203,
        5,16,0,0,203,204,5,6,0,0,204,205,3,72,36,0,205,206,5,4,0,0,206,207,
        5,17,0,0,207,208,5,6,0,0,208,209,3,74,37,0,209,13,1,0,0,0,210,211,
        5,19,0,0,211,212,5,20,0,0,212,213,3,54,27,0,213,15,1,0,0,0,214,223,
        3,18,9,0,215,223,3,20,10,0,216,223,3,22,11,0,217,223,3,24,12,0,218,
        223,3,26,13,0,219,223,3,28,14,0,220,223,3,30,15,0,221,223,3,32,16,
        0,222,214,1,0,0,0,222,215,1,0,0,0,222,216,1,0,0,0,222,217,1,0,0,
        0,222,218,1,0,0,0,222,219,1,0,0,0,222,220,1,0,0,0,222,221,1,0,0,
        0,223,17,1,0,0,0,224,225,5,21,0,0,225,226,5,22,0,0,226,227,3,46,
        23,0,227,228,5,23,0,0,228,229,5,24,0,0,229,230,5,6,0,0,230,231,3,
        92,46,0,231,232,5,25,0,0,232,235,3,54,27,0,233,234,5,4,0,0,234,236,
        3,62,31,0,235,233,1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,238,
        5,4,0,0,238,240,3,60,30,0,239,237,1,0,0,0,239,240,1,0,0,0,240,246,
        1,0,0,0,241,242,5,4,0,0,242,243,3,34,17,0,243,244,5,3,0,0,244,245,
        3,44,22,0,245,247,1,0,0,0,246,241,1,0,0,0,246,247,1,0,0,0,247,253,
        1,0,0,0,248,249,5,4,0,0,249,250,3,36,18,0,250,251,5,3,0,0,251,252,
        3,48,24,0,252,254,1,0,0,0,253,248,1,0,0,0,253,254,1,0,0,0,254,19,
        1,0,0,0,255,256,5,21,0,0,256,257,5,26,0,0,257,258,3,46,23,0,258,
        259,5,23,0,0,259,260,5,27,0,0,260,261,5,6,0,0,261,262,3,94,47,0,
        262,263,5,25,0,0,263,266,3,54,27,0,264,265,5,4,0,0,265,267,3,62,
        31,0,266,264,1,0,0,0,266,267,1,0,0,0,267,270,1,0,0,0,268,269,5,4,
        0,0,269,271,3,60,30,0,270,268,1,0,0,0,270,271,1,0,0,0,271,277,1,
        0,0,0,272,273,5,4,0,0,273,274,3,34,17,0,274,275,5,3,0,0,275,276,
        3,44,22,0,276,278,1,0,0,0,277,272,1,0,0,0,277,278,1,0,0,0,278,284,
        1,0,0,0,279,280,5,4,0,0,280,281,3,36,18,0,281,282,5,3,0,0,282,283,
        3,48,24,0,283,285,1,0,0,0,284,279,1,0,0,0,284,285,1,0,0,0,285,21,
        1,0,0,0,286,287,5,21,0,0,287,288,5,28,0,0,288,289,3,46,23,0,289,
        290,5,23,0,0,290,291,5,24,0,0,291,292,5,6,0,0,292,293,3,92,46,0,
        293,294,5,4,0,0,294,295,5,27,0,0,295,296,5,6,0,0,296,297,3,94,47,
        0,297,298,5,25,0,0,298,301,3,54,27,0,299,300,5,4,0,0,300,302,3,62,
        31,0,301,299,1,0,0,0,301,302,1,0,0,0,302,305,1,0,0,0,303,304,5,4,
        0,0,304,306,3,60,30,0,305,303,1,0,0,0,305,306,1,0,0,0,306,312,1,
        0,0,0,307,308,5,4,0,0,308,309,3,34,17,0,309,310,5,3,0,0,310,311,
        3,44,22,0,311,313,1,0,0,0,312,307,1,0,0,0,312,313,1,0,0,0,313,319,
        1,0,0,0,314,315,5,4,0,0,315,316,3,36,18,0,316,317,5,3,0,0,317,318,
        3,48,24,0,318,320,1,0,0,0,319,314,1,0,0,0,319,320,1,0,0,0,320,23,
        1,0,0,0,321,322,5,21,0,0,322,323,5,29,0,0,323,324,3,46,23,0,324,
        325,5,23,0,0,325,326,5,24,0,0,326,327,5,6,0,0,327,328,3,92,46,0,
        328,329,5,4,0,0,329,330,5,30,0,0,330,331,5,6,0,0,331,332,3,96,48,
        0,332,333,5,4,0,0,333,334,5,27,0,0,334,335,5,6,0,0,335,336,3,94,
        47,0,336,337,5,25,0,0,337,340,3,54,27,0,338,339,5,4,0,0,339,341,
        3,62,31,0,340,338,1,0,0,0,340,341,1,0,0,0,341,344,1,0,0,0,342,343,
        5,4,0,0,343,345,3,60,30,0,344,342,1,0,0,0,344,345,1,0,0,0,345,351,
        1,0,0,0,346,347,5,4,0,0,347,348,3,34,17,0,348,349,5,3,0,0,349,350,
        3,44,22,0,350,352,1,0,0,0,351,346,1,0,0,0,351,352,1,0,0,0,352,358,
        1,0,0,0,353,354,5,4,0,0,354,355,3,36,18,0,355,356,5,3,0,0,356,357,
        3,48,24,0,357,359,1,0,0,0,358,353,1,0,0,0,358,359,1,0,0,0,359,25,
        1,0,0,0,360,361,5,21,0,0,361,362,5,31,0,0,362,363,3,46,23,0,363,
        364,5,23,0,0,364,365,5,24,0,0,365,366,5,6,0,0,366,367,3,92,46,0,
        367,368,5,4,0,0,368,369,5,30,0,0,369,370,5,6,0,0,370,371,3,96,48,
        0,371,372,5,4,0,0,372,373,5,27,0,0,373,374,5,6,0,0,374,375,3,94,
        47,0,375,376,5,25,0,0,376,377,5,23,0,0,377,378,5,32,0,0,378,379,
        5,6,0,0,379,380,3,98,49,0,380,381,5,4,0,0,381,382,5,33,0,0,382,383,
        5,6,0,0,383,384,3,102,51,0,384,385,5,4,0,0,385,386,5,34,0,0,386,
        387,5,6,0,0,387,388,3,100,50,0,388,389,5,4,0,0,389,390,5,35,0,0,
        390,391,5,6,0,0,391,392,3,104,52,0,392,393,5,25,0,0,393,396,3,54,
        27,0,394,395,5,4,0,0,395,397,3,62,31,0,396,394,1,0,0,0,396,397,1,
        0,0,0,397,400,1,0,0,0,398,399,5,4,0,0,399,401,3,60,30,0,400,398,
        1,0,0,0,400,401,1,0,0,0,401,407,1,0,0,0,402,403,5,4,0,0,403,404,
        3,34,17,0,404,405,5,3,0,0,405,406,3,44,22,0,406,408,1,0,0,0,407,
        402,1,0,0,0,407,408,1,0,0,0,408,414,1,0,0,0,409,410,5,4,0,0,410,
        411,3,36,18,0,411,412,5,3,0,0,412,413,3,48,24,0,413,415,1,0,0,0,
        414,409,1,0,0,0,414,415,1,0,0,0,415,27,1,0,0,0,416,417,5,21,0,0,
        417,418,5,36,0,0,418,419,3,46,23,0,419,420,5,23,0,0,420,421,5,24,
        0,0,421,422,5,6,0,0,422,423,3,92,46,0,423,424,5,25,0,0,424,427,3,
        54,27,0,425,426,5,4,0,0,426,428,3,62,31,0,427,425,1,0,0,0,427,428,
        1,0,0,0,428,431,1,0,0,0,429,430,5,4,0,0,430,432,3,60,30,0,431,429,
        1,0,0,0,431,432,1,0,0,0,432,438,1,0,0,0,433,434,5,4,0,0,434,435,
        3,34,17,0,435,436,5,3,0,0,436,437,3,44,22,0,437,439,1,0,0,0,438,
        433,1,0,0,0,438,439,1,0,0,0,439,445,1,0,0,0,440,441,5,4,0,0,441,
        442,3,36,18,0,442,443,5,3,0,0,443,444,3,48,24,0,444,446,1,0,0,0,
        445,440,1,0,0,0,445,446,1,0,0,0,446,29,1,0,0,0,447,448,5,21,0,0,
        448,449,5,37,0,0,449,450,3,46,23,0,450,451,5,23,0,0,451,452,5,24,
        0,0,452,453,5,6,0,0,453,454,3,92,46,0,454,455,5,4,0,0,455,456,5,
        27,0,0,456,457,5,6,0,0,457,458,3,94,47,0,458,459,5,25,0,0,459,462,
        3,54,27,0,460,461,5,4,0,0,461,463,3,62,31,0,462,460,1,0,0,0,462,
        463,1,0,0,0,463,466,1,0,0,0,464,465,5,4,0,0,465,467,3,60,30,0,466,
        464,1,0,0,0,466,467,1,0,0,0,467,473,1,0,0,0,468,469,5,4,0,0,469,
        470,3,34,17,0,470,471,5,3,0,0,471,472,3,44,22,0,472,474,1,0,0,0,
        473,468,1,0,0,0,473,474,1,0,0,0,474,480,1,0,0,0,475,476,5,4,0,0,
        476,477,3,36,18,0,477,478,5,3,0,0,478,479,3,48,24,0,479,481,1,0,
        0,0,480,475,1,0,0,0,480,481,1,0,0,0,481,31,1,0,0,0,482,483,5,21,
        0,0,483,484,5,38,0,0,484,485,3,46,23,0,485,486,5,23,0,0,486,487,
        5,39,0,0,487,488,5,6,0,0,488,489,3,76,38,0,489,490,5,4,0,0,490,491,
        5,40,0,0,491,492,5,6,0,0,492,493,3,78,39,0,493,494,5,4,0,0,494,495,
        5,41,0,0,495,496,5,6,0,0,496,497,3,80,40,0,497,498,5,4,0,0,498,499,
        5,42,0,0,499,500,5,6,0,0,500,501,3,82,41,0,501,502,5,4,0,0,502,503,
        5,43,0,0,503,504,5,6,0,0,504,505,3,84,42,0,505,506,5,4,0,0,506,507,
        5,44,0,0,507,508,5,6,0,0,508,509,3,84,42,0,509,510,5,4,0,0,510,511,
        5,45,0,0,511,512,5,6,0,0,512,513,3,86,43,0,513,514,5,4,0,0,514,515,
        5,46,0,0,515,516,5,6,0,0,516,517,3,88,44,0,517,518,5,4,0,0,518,519,
        5,47,0,0,519,520,5,6,0,0,520,521,3,90,45,0,521,522,5,25,0,0,522,
        525,3,54,27,0,523,524,5,4,0,0,524,526,3,62,31,0,525,523,1,0,0,0,
        525,526,1,0,0,0,526,529,1,0,0,0,527,528,5,4,0,0,528,530,3,60,30,
        0,529,527,1,0,0,0,529,530,1,0,0,0,530,536,1,0,0,0,531,532,5,4,0,
        0,532,533,3,34,17,0,533,534,5,3,0,0,534,535,3,44,22,0,535,537,1,
        0,0,0,536,531,1,0,0,0,536,537,1,0,0,0,537,543,1,0,0,0,538,539,5,
        4,0,0,539,540,3,36,18,0,540,541,5,3,0,0,541,542,3,48,24,0,542,544,
        1,0,0,0,543,538,1,0,0,0,543,544,1,0,0,0,544,33,1,0,0,0,545,546,5,
        48,0,0,546,547,5,21,0,0,547,35,1,0,0,0,548,549,5,48,0,0,549,550,
        5,49,0,0,550,37,1,0,0,0,551,552,7,0,0,0,552,39,1,0,0,0,553,554,5,
        63,0,0,554,41,1,0,0,0,555,556,5,62,0,0,556,43,1,0,0,0,557,558,5,
        63,0,0,558,45,1,0,0,0,559,560,5,62,0,0,560,47,1,0,0,0,561,562,5,
        63,0,0,562,49,1,0,0,0,563,564,5,63,0,0,564,51,1,0,0,0,565,566,5,
        63,0,0,566,53,1,0,0,0,567,568,5,62,0,0,568,55,1,0,0,0,569,570,5,
        58,0,0,570,57,1,0,0,0,571,572,5,58,0,0,572,59,1,0,0,0,573,574,5,
        10,0,0,574,61,1,0,0,0,575,576,5,55,0,0,576,63,1,0,0,0,577,578,5,
        61,0,0,578,65,1,0,0,0,579,580,5,63,0,0,580,67,1,0,0,0,581,582,5,
        58,0,0,582,69,1,0,0,0,583,584,5,58,0,0,584,71,1,0,0,0,585,586,5,
        59,0,0,586,73,1,0,0,0,587,588,7,1,0,0,588,75,1,0,0,0,589,590,5,59,
        0,0,590,77,1,0,0,0,591,592,5,59,0,0,592,79,1,0,0,0,593,594,5,59,
        0,0,594,81,1,0,0,0,595,596,5,60,0,0,596,83,1,0,0,0,597,598,5,59,
        0,0,598,85,1,0,0,0,599,600,5,63,0,0,600,87,1,0,0,0,601,602,5,63,
        0,0,602,89,1,0,0,0,603,604,5,59,0,0,604,91,1,0,0,0,605,606,5,59,
        0,0,606,93,1,0,0,0,607,608,5,59,0,0,608,95,1,0,0,0,609,610,5,59,
        0,0,610,97,1,0,0,0,611,612,5,59,0,0,612,99,1,0,0,0,613,614,5,59,
        0,0,614,101,1,0,0,0,615,616,5,59,0,0,616,103,1,0,0,0,617,618,5,59,
        0,0,618,105,1,0,0,0,37,112,120,147,182,222,235,239,246,253,266,270,
        277,284,301,305,312,319,340,344,351,358,396,400,407,414,427,431,
        438,445,462,466,473,480,525,529,536,543
    ]

class TimelyParser ( Parser ):

    grammarFileName = "Timely.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'data'", "'as'", "','", "'time'", 
                     "'='", "'value'", "'trainEnd'", "'testEnd'", "'visualize'", 
                     "'ticker'", "'interval'", "'start'", "'end'", "'acf'", 
                     "'lags'", "'type'", "'pacf'", "'test'", "'adf'", "'model'", 
                     "'AR'", "'('", "'p'", "')'", "'MA'", "'q'", "'ARMA'", 
                     "'ARIMA'", "'d'", "'SARIMA'", "'P'", "'D'", "'Q'", 
                     "'s'", "'ARCH'", "'GARCH'", "'lstm'", "'n_layers'", 
                     "'batch_size'", "'n_epochs'", "'drop_out'", "'lstm_neurons'", 
                     "'dense_neurons'", "'optimizer'", "'loss'", "'seq_length'", 
                     "'save'", "'chart'", "'Open'", "'High'", "'Low'", "'Close'", 
                     "'Adj Close'", "'summary'", "'Plot'", "'Bar'" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "DATE", "INT", "FLOAT", 
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
    RULE_ar_model = 9
    RULE_ma_model = 10
    RULE_arma_model = 11
    RULE_arima_model = 12
    RULE_sarima_model = 13
    RULE_arch_model = 14
    RULE_garch_model = 15
    RULE_lstm_model = 16
    RULE_save_model = 17
    RULE_save_chart = 18
    RULE_price_value = 19
    RULE_coin_name = 20
    RULE_ticker_name = 21
    RULE_model_name = 22
    RULE_model = 23
    RULE_chart_name = 24
    RULE_time = 25
    RULE_value = 26
    RULE_dataframe_name = 27
    RULE_train_end = 28
    RULE_test_end = 29
    RULE_visualize = 30
    RULE_summary = 31
    RULE_visualize_bool = 32
    RULE_interval = 33
    RULE_start_time = 34
    RULE_end_time = 35
    RULE_lags = 36
    RULE_type = 37
    RULE_n_layers = 38
    RULE_batch_size = 39
    RULE_n_epochs = 40
    RULE_drop_out = 41
    RULE_lstm_neurons = 42
    RULE_optimizer = 43
    RULE_loss = 44
    RULE_seq_length = 45
    RULE_p = 46
    RULE_q = 47
    RULE_d = 48
    RULE_ps = 49
    RULE_qs = 50
    RULE_ds = 51
    RULE_s = 52

    ruleNames =  [ "start", "program", "statement", "dataframeLoadStatement", 
                   "tickerLoadStatement", "acfStatement", "pacfStatement", 
                   "testStatement", "modelStatement", "ar_model", "ma_model", 
                   "arma_model", "arima_model", "sarima_model", "arch_model", 
                   "garch_model", "lstm_model", "save_model", "save_chart", 
                   "price_value", "coin_name", "ticker_name", "model_name", 
                   "model", "chart_name", "time", "value", "dataframe_name", 
                   "train_end", "test_end", "visualize", "summary", "visualize_bool", 
                   "interval", "start_time", "end_time", "lags", "type", 
                   "n_layers", "batch_size", "n_epochs", "drop_out", "lstm_neurons", 
                   "optimizer", "loss", "seq_length", "p", "q", "d", "ps", 
                   "qs", "ds", "s" ]

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
    T__54=55
    T__55=56
    T__56=57
    DATE=58
    INT=59
    FLOAT=60
    BOOL=61
    ID=62
    STRING=63
    WS=64
    COMMENT=65

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
            self.state = 106
            self.program()
            self.state = 107
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
            self.state = 110 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 109
                self.statement()
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2916354) != 0)):
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.dataframeLoadStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.tickerLoadStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.acfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.pacfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 118
                self.testStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 119
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

        def dataframe_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TimelyParser.Dataframe_nameContext)
            else:
                return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,i)


        def time(self):
            return self.getTypedRuleContext(TimelyParser.TimeContext,0)


        def value(self):
            return self.getTypedRuleContext(TimelyParser.ValueContext,0)


        def train_end(self):
            return self.getTypedRuleContext(TimelyParser.Train_endContext,0)


        def test_end(self):
            return self.getTypedRuleContext(TimelyParser.Test_endContext,0)


        def visualize_bool(self):
            return self.getTypedRuleContext(TimelyParser.Visualize_boolContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(TimelyParser.T__0)
            self.state = 123
            self.match(TimelyParser.T__1)
            self.state = 124
            self.dataframe_name()
            self.state = 125
            self.match(TimelyParser.T__2)
            self.state = 126
            self.dataframe_name()
            self.state = 127
            self.match(TimelyParser.T__3)
            self.state = 128
            self.match(TimelyParser.T__4)
            self.state = 129
            self.match(TimelyParser.T__5)
            self.state = 130
            self.time()
            self.state = 131
            self.match(TimelyParser.T__3)
            self.state = 132
            self.match(TimelyParser.T__6)
            self.state = 133
            self.match(TimelyParser.T__5)
            self.state = 134
            self.value()
            self.state = 135
            self.match(TimelyParser.T__3)
            self.state = 136
            self.match(TimelyParser.T__7)
            self.state = 137
            self.match(TimelyParser.T__5)
            self.state = 138
            self.train_end()
            self.state = 139
            self.match(TimelyParser.T__3)
            self.state = 140
            self.match(TimelyParser.T__8)
            self.state = 141
            self.match(TimelyParser.T__5)
            self.state = 142
            self.test_end()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 143
                self.match(TimelyParser.T__3)
                self.state = 144
                self.match(TimelyParser.T__9)
                self.state = 145
                self.match(TimelyParser.T__5)
                self.state = 146
                self.visualize_bool()


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

        def coin_name(self):
            return self.getTypedRuleContext(TimelyParser.Coin_nameContext,0)


        def dataframe_name(self):
            return self.getTypedRuleContext(TimelyParser.Dataframe_nameContext,0)


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


        def visualize_bool(self):
            return self.getTypedRuleContext(TimelyParser.Visualize_boolContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(TimelyParser.T__0)
            self.state = 150
            self.match(TimelyParser.T__10)
            self.state = 151
            self.coin_name()
            self.state = 152
            self.match(TimelyParser.T__2)
            self.state = 153
            self.dataframe_name()
            self.state = 154
            self.match(TimelyParser.T__3)
            self.state = 155
            self.match(TimelyParser.T__11)
            self.state = 156
            self.match(TimelyParser.T__5)
            self.state = 157
            self.interval()
            self.state = 158
            self.match(TimelyParser.T__3)
            self.state = 159
            self.match(TimelyParser.T__12)
            self.state = 160
            self.match(TimelyParser.T__5)
            self.state = 161
            self.start_time()
            self.state = 162
            self.match(TimelyParser.T__3)
            self.state = 163
            self.match(TimelyParser.T__13)
            self.state = 164
            self.match(TimelyParser.T__5)
            self.state = 165
            self.end_time()
            self.state = 166
            self.match(TimelyParser.T__3)
            self.state = 167
            self.match(TimelyParser.T__6)
            self.state = 168
            self.match(TimelyParser.T__5)
            self.state = 169
            self.price_value()
            self.state = 170
            self.match(TimelyParser.T__3)
            self.state = 171
            self.match(TimelyParser.T__7)
            self.state = 172
            self.match(TimelyParser.T__5)
            self.state = 173
            self.train_end()
            self.state = 174
            self.match(TimelyParser.T__3)
            self.state = 175
            self.match(TimelyParser.T__8)
            self.state = 176
            self.match(TimelyParser.T__5)
            self.state = 177
            self.test_end()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 178
                self.match(TimelyParser.T__3)
                self.state = 179
                self.match(TimelyParser.T__9)
                self.state = 180
                self.match(TimelyParser.T__5)
                self.state = 181
                self.visualize_bool()


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
            self.state = 184
            self.match(TimelyParser.T__14)
            self.state = 185
            self.match(TimelyParser.T__1)
            self.state = 186
            self.match(TimelyParser.T__5)
            self.state = 187
            self.dataframe_name()
            self.state = 188
            self.match(TimelyParser.T__3)
            self.state = 189
            self.match(TimelyParser.T__15)
            self.state = 190
            self.match(TimelyParser.T__5)
            self.state = 191
            self.lags()
            self.state = 192
            self.match(TimelyParser.T__3)
            self.state = 193
            self.match(TimelyParser.T__16)
            self.state = 194
            self.match(TimelyParser.T__5)
            self.state = 195
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
            self.state = 197
            self.match(TimelyParser.T__17)
            self.state = 198
            self.match(TimelyParser.T__1)
            self.state = 199
            self.match(TimelyParser.T__5)
            self.state = 200
            self.dataframe_name()
            self.state = 201
            self.match(TimelyParser.T__3)
            self.state = 202
            self.match(TimelyParser.T__15)
            self.state = 203
            self.match(TimelyParser.T__5)
            self.state = 204
            self.lags()
            self.state = 205
            self.match(TimelyParser.T__3)
            self.state = 206
            self.match(TimelyParser.T__16)
            self.state = 207
            self.match(TimelyParser.T__5)
            self.state = 208
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
            self.state = 210
            self.match(TimelyParser.T__18)
            self.state = 211
            self.match(TimelyParser.T__19)
            self.state = 212
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

        def ar_model(self):
            return self.getTypedRuleContext(TimelyParser.Ar_modelContext,0)


        def ma_model(self):
            return self.getTypedRuleContext(TimelyParser.Ma_modelContext,0)


        def arma_model(self):
            return self.getTypedRuleContext(TimelyParser.Arma_modelContext,0)


        def arima_model(self):
            return self.getTypedRuleContext(TimelyParser.Arima_modelContext,0)


        def sarima_model(self):
            return self.getTypedRuleContext(TimelyParser.Sarima_modelContext,0)


        def arch_model(self):
            return self.getTypedRuleContext(TimelyParser.Arch_modelContext,0)


        def garch_model(self):
            return self.getTypedRuleContext(TimelyParser.Garch_modelContext,0)


        def lstm_model(self):
            return self.getTypedRuleContext(TimelyParser.Lstm_modelContext,0)


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
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.ar_model()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.ma_model()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.arma_model()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.arima_model()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 218
                self.sarima_model()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 219
                self.arch_model()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 220
                self.garch_model()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 221
                self.lstm_model()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ar_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_ar_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAr_model" ):
                listener.enterAr_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAr_model" ):
                listener.exitAr_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAr_model" ):
                return visitor.visitAr_model(self)
            else:
                return visitor.visitChildren(self)




    def ar_model(self):

        localctx = TimelyParser.Ar_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ar_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(TimelyParser.T__20)
            self.state = 225
            self.match(TimelyParser.T__21)
            self.state = 226
            self.model()
            self.state = 227
            self.match(TimelyParser.T__22)
            self.state = 228
            self.match(TimelyParser.T__23)
            self.state = 229
            self.match(TimelyParser.T__5)
            self.state = 230
            self.p()
            self.state = 231
            self.match(TimelyParser.T__24)
            self.state = 232
            self.dataframe_name()
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 233
                self.match(TimelyParser.T__3)
                self.state = 234
                self.summary()


            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(TimelyParser.T__3)
                self.state = 238
                self.visualize()


            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(TimelyParser.T__3)
                self.state = 242
                self.save_model()
                self.state = 243
                self.match(TimelyParser.T__2)
                self.state = 244
                self.model_name()


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 248
                self.match(TimelyParser.T__3)
                self.state = 249
                self.save_chart()
                self.state = 250
                self.match(TimelyParser.T__2)
                self.state = 251
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ma_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


        def q(self):
            return self.getTypedRuleContext(TimelyParser.QContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_ma_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMa_model" ):
                listener.enterMa_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMa_model" ):
                listener.exitMa_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMa_model" ):
                return visitor.visitMa_model(self)
            else:
                return visitor.visitChildren(self)




    def ma_model(self):

        localctx = TimelyParser.Ma_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ma_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(TimelyParser.T__20)
            self.state = 256
            self.match(TimelyParser.T__25)
            self.state = 257
            self.model()
            self.state = 258
            self.match(TimelyParser.T__22)
            self.state = 259
            self.match(TimelyParser.T__26)
            self.state = 260
            self.match(TimelyParser.T__5)
            self.state = 261
            self.q()
            self.state = 262
            self.match(TimelyParser.T__24)
            self.state = 263
            self.dataframe_name()
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 264
                self.match(TimelyParser.T__3)
                self.state = 265
                self.summary()


            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(TimelyParser.T__3)
                self.state = 269
                self.visualize()


            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 272
                self.match(TimelyParser.T__3)
                self.state = 273
                self.save_model()
                self.state = 274
                self.match(TimelyParser.T__2)
                self.state = 275
                self.model_name()


            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 279
                self.match(TimelyParser.T__3)
                self.state = 280
                self.save_chart()
                self.state = 281
                self.match(TimelyParser.T__2)
                self.state = 282
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arma_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


        def p(self):
            return self.getTypedRuleContext(TimelyParser.PContext,0)


        def q(self):
            return self.getTypedRuleContext(TimelyParser.QContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_arma_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArma_model" ):
                listener.enterArma_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArma_model" ):
                listener.exitArma_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArma_model" ):
                return visitor.visitArma_model(self)
            else:
                return visitor.visitChildren(self)




    def arma_model(self):

        localctx = TimelyParser.Arma_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arma_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(TimelyParser.T__20)
            self.state = 287
            self.match(TimelyParser.T__27)
            self.state = 288
            self.model()
            self.state = 289
            self.match(TimelyParser.T__22)
            self.state = 290
            self.match(TimelyParser.T__23)
            self.state = 291
            self.match(TimelyParser.T__5)
            self.state = 292
            self.p()
            self.state = 293
            self.match(TimelyParser.T__3)
            self.state = 294
            self.match(TimelyParser.T__26)
            self.state = 295
            self.match(TimelyParser.T__5)
            self.state = 296
            self.q()
            self.state = 297
            self.match(TimelyParser.T__24)
            self.state = 298
            self.dataframe_name()
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 299
                self.match(TimelyParser.T__3)
                self.state = 300
                self.summary()


            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 303
                self.match(TimelyParser.T__3)
                self.state = 304
                self.visualize()


            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 307
                self.match(TimelyParser.T__3)
                self.state = 308
                self.save_model()
                self.state = 309
                self.match(TimelyParser.T__2)
                self.state = 310
                self.model_name()


            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 314
                self.match(TimelyParser.T__3)
                self.state = 315
                self.save_chart()
                self.state = 316
                self.match(TimelyParser.T__2)
                self.state = 317
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arima_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


        def p(self):
            return self.getTypedRuleContext(TimelyParser.PContext,0)


        def d(self):
            return self.getTypedRuleContext(TimelyParser.DContext,0)


        def q(self):
            return self.getTypedRuleContext(TimelyParser.QContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_arima_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArima_model" ):
                listener.enterArima_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArima_model" ):
                listener.exitArima_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArima_model" ):
                return visitor.visitArima_model(self)
            else:
                return visitor.visitChildren(self)




    def arima_model(self):

        localctx = TimelyParser.Arima_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arima_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(TimelyParser.T__20)
            self.state = 322
            self.match(TimelyParser.T__28)
            self.state = 323
            self.model()
            self.state = 324
            self.match(TimelyParser.T__22)
            self.state = 325
            self.match(TimelyParser.T__23)
            self.state = 326
            self.match(TimelyParser.T__5)
            self.state = 327
            self.p()
            self.state = 328
            self.match(TimelyParser.T__3)
            self.state = 329
            self.match(TimelyParser.T__29)
            self.state = 330
            self.match(TimelyParser.T__5)
            self.state = 331
            self.d()
            self.state = 332
            self.match(TimelyParser.T__3)
            self.state = 333
            self.match(TimelyParser.T__26)
            self.state = 334
            self.match(TimelyParser.T__5)
            self.state = 335
            self.q()
            self.state = 336
            self.match(TimelyParser.T__24)
            self.state = 337
            self.dataframe_name()
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 338
                self.match(TimelyParser.T__3)
                self.state = 339
                self.summary()


            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 342
                self.match(TimelyParser.T__3)
                self.state = 343
                self.visualize()


            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 346
                self.match(TimelyParser.T__3)
                self.state = 347
                self.save_model()
                self.state = 348
                self.match(TimelyParser.T__2)
                self.state = 349
                self.model_name()


            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 353
                self.match(TimelyParser.T__3)
                self.state = 354
                self.save_chart()
                self.state = 355
                self.match(TimelyParser.T__2)
                self.state = 356
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sarima_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


        def p(self):
            return self.getTypedRuleContext(TimelyParser.PContext,0)


        def d(self):
            return self.getTypedRuleContext(TimelyParser.DContext,0)


        def q(self):
            return self.getTypedRuleContext(TimelyParser.QContext,0)


        def ps(self):
            return self.getTypedRuleContext(TimelyParser.PsContext,0)


        def ds(self):
            return self.getTypedRuleContext(TimelyParser.DsContext,0)


        def qs(self):
            return self.getTypedRuleContext(TimelyParser.QsContext,0)


        def s(self):
            return self.getTypedRuleContext(TimelyParser.SContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_sarima_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSarima_model" ):
                listener.enterSarima_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSarima_model" ):
                listener.exitSarima_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSarima_model" ):
                return visitor.visitSarima_model(self)
            else:
                return visitor.visitChildren(self)




    def sarima_model(self):

        localctx = TimelyParser.Sarima_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sarima_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(TimelyParser.T__20)
            self.state = 361
            self.match(TimelyParser.T__30)
            self.state = 362
            self.model()
            self.state = 363
            self.match(TimelyParser.T__22)
            self.state = 364
            self.match(TimelyParser.T__23)
            self.state = 365
            self.match(TimelyParser.T__5)
            self.state = 366
            self.p()
            self.state = 367
            self.match(TimelyParser.T__3)
            self.state = 368
            self.match(TimelyParser.T__29)
            self.state = 369
            self.match(TimelyParser.T__5)
            self.state = 370
            self.d()
            self.state = 371
            self.match(TimelyParser.T__3)
            self.state = 372
            self.match(TimelyParser.T__26)
            self.state = 373
            self.match(TimelyParser.T__5)
            self.state = 374
            self.q()
            self.state = 375
            self.match(TimelyParser.T__24)
            self.state = 376
            self.match(TimelyParser.T__22)
            self.state = 377
            self.match(TimelyParser.T__31)
            self.state = 378
            self.match(TimelyParser.T__5)
            self.state = 379
            self.ps()
            self.state = 380
            self.match(TimelyParser.T__3)
            self.state = 381
            self.match(TimelyParser.T__32)
            self.state = 382
            self.match(TimelyParser.T__5)
            self.state = 383
            self.ds()
            self.state = 384
            self.match(TimelyParser.T__3)
            self.state = 385
            self.match(TimelyParser.T__33)
            self.state = 386
            self.match(TimelyParser.T__5)
            self.state = 387
            self.qs()
            self.state = 388
            self.match(TimelyParser.T__3)
            self.state = 389
            self.match(TimelyParser.T__34)
            self.state = 390
            self.match(TimelyParser.T__5)
            self.state = 391
            self.s()
            self.state = 392
            self.match(TimelyParser.T__24)
            self.state = 393
            self.dataframe_name()
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 394
                self.match(TimelyParser.T__3)
                self.state = 395
                self.summary()


            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 398
                self.match(TimelyParser.T__3)
                self.state = 399
                self.visualize()


            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 402
                self.match(TimelyParser.T__3)
                self.state = 403
                self.save_model()
                self.state = 404
                self.match(TimelyParser.T__2)
                self.state = 405
                self.model_name()


            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 409
                self.match(TimelyParser.T__3)
                self.state = 410
                self.save_chart()
                self.state = 411
                self.match(TimelyParser.T__2)
                self.state = 412
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arch_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_arch_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArch_model" ):
                listener.enterArch_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArch_model" ):
                listener.exitArch_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArch_model" ):
                return visitor.visitArch_model(self)
            else:
                return visitor.visitChildren(self)




    def arch_model(self):

        localctx = TimelyParser.Arch_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arch_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(TimelyParser.T__20)
            self.state = 417
            self.match(TimelyParser.T__35)
            self.state = 418
            self.model()
            self.state = 419
            self.match(TimelyParser.T__22)
            self.state = 420
            self.match(TimelyParser.T__23)
            self.state = 421
            self.match(TimelyParser.T__5)
            self.state = 422
            self.p()
            self.state = 423
            self.match(TimelyParser.T__24)
            self.state = 424
            self.dataframe_name()
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 425
                self.match(TimelyParser.T__3)
                self.state = 426
                self.summary()


            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 429
                self.match(TimelyParser.T__3)
                self.state = 430
                self.visualize()


            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 433
                self.match(TimelyParser.T__3)
                self.state = 434
                self.save_model()
                self.state = 435
                self.match(TimelyParser.T__2)
                self.state = 436
                self.model_name()


            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 440
                self.match(TimelyParser.T__3)
                self.state = 441
                self.save_chart()
                self.state = 442
                self.match(TimelyParser.T__2)
                self.state = 443
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Garch_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


        def p(self):
            return self.getTypedRuleContext(TimelyParser.PContext,0)


        def q(self):
            return self.getTypedRuleContext(TimelyParser.QContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_garch_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGarch_model" ):
                listener.enterGarch_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGarch_model" ):
                listener.exitGarch_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGarch_model" ):
                return visitor.visitGarch_model(self)
            else:
                return visitor.visitChildren(self)




    def garch_model(self):

        localctx = TimelyParser.Garch_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_garch_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(TimelyParser.T__20)
            self.state = 448
            self.match(TimelyParser.T__36)
            self.state = 449
            self.model()
            self.state = 450
            self.match(TimelyParser.T__22)
            self.state = 451
            self.match(TimelyParser.T__23)
            self.state = 452
            self.match(TimelyParser.T__5)
            self.state = 453
            self.p()
            self.state = 454
            self.match(TimelyParser.T__3)
            self.state = 455
            self.match(TimelyParser.T__26)
            self.state = 456
            self.match(TimelyParser.T__5)
            self.state = 457
            self.q()
            self.state = 458
            self.match(TimelyParser.T__24)
            self.state = 459
            self.dataframe_name()
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 460
                self.match(TimelyParser.T__3)
                self.state = 461
                self.summary()


            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 464
                self.match(TimelyParser.T__3)
                self.state = 465
                self.visualize()


            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 468
                self.match(TimelyParser.T__3)
                self.state = 469
                self.save_model()
                self.state = 470
                self.match(TimelyParser.T__2)
                self.state = 471
                self.model_name()


            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 475
                self.match(TimelyParser.T__3)
                self.state = 476
                self.save_chart()
                self.state = 477
                self.match(TimelyParser.T__2)
                self.state = 478
                self.chart_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lstm_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(TimelyParser.ModelContext,0)


        def n_layers(self):
            return self.getTypedRuleContext(TimelyParser.N_layersContext,0)


        def batch_size(self):
            return self.getTypedRuleContext(TimelyParser.Batch_sizeContext,0)


        def n_epochs(self):
            return self.getTypedRuleContext(TimelyParser.N_epochsContext,0)


        def drop_out(self):
            return self.getTypedRuleContext(TimelyParser.Drop_outContext,0)


        def lstm_neurons(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TimelyParser.Lstm_neuronsContext)
            else:
                return self.getTypedRuleContext(TimelyParser.Lstm_neuronsContext,i)


        def optimizer(self):
            return self.getTypedRuleContext(TimelyParser.OptimizerContext,0)


        def loss(self):
            return self.getTypedRuleContext(TimelyParser.LossContext,0)


        def seq_length(self):
            return self.getTypedRuleContext(TimelyParser.Seq_lengthContext,0)


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


        def getRuleIndex(self):
            return TimelyParser.RULE_lstm_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLstm_model" ):
                listener.enterLstm_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLstm_model" ):
                listener.exitLstm_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLstm_model" ):
                return visitor.visitLstm_model(self)
            else:
                return visitor.visitChildren(self)




    def lstm_model(self):

        localctx = TimelyParser.Lstm_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lstm_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(TimelyParser.T__20)
            self.state = 483
            self.match(TimelyParser.T__37)
            self.state = 484
            self.model()
            self.state = 485
            self.match(TimelyParser.T__22)
            self.state = 486
            self.match(TimelyParser.T__38)
            self.state = 487
            self.match(TimelyParser.T__5)
            self.state = 488
            self.n_layers()
            self.state = 489
            self.match(TimelyParser.T__3)
            self.state = 490
            self.match(TimelyParser.T__39)
            self.state = 491
            self.match(TimelyParser.T__5)
            self.state = 492
            self.batch_size()
            self.state = 493
            self.match(TimelyParser.T__3)
            self.state = 494
            self.match(TimelyParser.T__40)
            self.state = 495
            self.match(TimelyParser.T__5)
            self.state = 496
            self.n_epochs()
            self.state = 497
            self.match(TimelyParser.T__3)
            self.state = 498
            self.match(TimelyParser.T__41)
            self.state = 499
            self.match(TimelyParser.T__5)
            self.state = 500
            self.drop_out()
            self.state = 501
            self.match(TimelyParser.T__3)
            self.state = 502
            self.match(TimelyParser.T__42)
            self.state = 503
            self.match(TimelyParser.T__5)
            self.state = 504
            self.lstm_neurons()
            self.state = 505
            self.match(TimelyParser.T__3)
            self.state = 506
            self.match(TimelyParser.T__43)
            self.state = 507
            self.match(TimelyParser.T__5)
            self.state = 508
            self.lstm_neurons()
            self.state = 509
            self.match(TimelyParser.T__3)
            self.state = 510
            self.match(TimelyParser.T__44)
            self.state = 511
            self.match(TimelyParser.T__5)
            self.state = 512
            self.optimizer()
            self.state = 513
            self.match(TimelyParser.T__3)
            self.state = 514
            self.match(TimelyParser.T__45)
            self.state = 515
            self.match(TimelyParser.T__5)
            self.state = 516
            self.loss()
            self.state = 517
            self.match(TimelyParser.T__3)
            self.state = 518
            self.match(TimelyParser.T__46)
            self.state = 519
            self.match(TimelyParser.T__5)
            self.state = 520
            self.seq_length()
            self.state = 521
            self.match(TimelyParser.T__24)
            self.state = 522
            self.dataframe_name()
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 523
                self.match(TimelyParser.T__3)
                self.state = 524
                self.summary()


            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 527
                self.match(TimelyParser.T__3)
                self.state = 528
                self.visualize()


            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 531
                self.match(TimelyParser.T__3)
                self.state = 532
                self.save_model()
                self.state = 533
                self.match(TimelyParser.T__2)
                self.state = 534
                self.model_name()


            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 538
                self.match(TimelyParser.T__3)
                self.state = 539
                self.save_chart()
                self.state = 540
                self.match(TimelyParser.T__2)
                self.state = 541
                self.chart_name()


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
        self.enterRule(localctx, 34, self.RULE_save_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(TimelyParser.T__47)
            self.state = 546
            self.match(TimelyParser.T__20)
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
        self.enterRule(localctx, 36, self.RULE_save_chart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(TimelyParser.T__47)
            self.state = 549
            self.match(TimelyParser.T__48)
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
        self.enterRule(localctx, 38, self.RULE_price_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34902897112121344) != 0)):
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


    class Coin_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_coin_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoin_name" ):
                listener.enterCoin_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoin_name" ):
                listener.exitCoin_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoin_name" ):
                return visitor.visitCoin_name(self)
            else:
                return visitor.visitChildren(self)




    def coin_name(self):

        localctx = TimelyParser.Coin_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_coin_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(TimelyParser.STRING)
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
        self.enterRule(localctx, 42, self.RULE_ticker_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
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
        self.enterRule(localctx, 44, self.RULE_model_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TimelyParser.ID, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = TimelyParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(TimelyParser.ID)
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
        self.enterRule(localctx, 48, self.RULE_chart_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
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
        self.enterRule(localctx, 50, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
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
        self.enterRule(localctx, 52, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
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
        self.enterRule(localctx, 54, self.RULE_dataframe_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
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
        self.enterRule(localctx, 56, self.RULE_train_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
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
        self.enterRule(localctx, 58, self.RULE_test_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
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
        self.enterRule(localctx, 60, self.RULE_visualize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(TimelyParser.T__9)
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
        self.enterRule(localctx, 62, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.match(TimelyParser.T__54)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Visualize_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(TimelyParser.BOOL, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_visualize_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualize_bool" ):
                listener.enterVisualize_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualize_bool" ):
                listener.exitVisualize_bool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualize_bool" ):
                return visitor.visitVisualize_bool(self)
            else:
                return visitor.visitChildren(self)




    def visualize_bool(self):

        localctx = TimelyParser.Visualize_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_visualize_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
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

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

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
        self.enterRule(localctx, 66, self.RULE_interval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(TimelyParser.STRING)
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
        self.enterRule(localctx, 68, self.RULE_start_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
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
        self.enterRule(localctx, 70, self.RULE_end_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
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
        self.enterRule(localctx, 72, self.RULE_lags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
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
        self.enterRule(localctx, 74, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not(_la==56 or _la==57):
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


    class N_layersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_n_layers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN_layers" ):
                listener.enterN_layers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN_layers" ):
                listener.exitN_layers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_layers" ):
                return visitor.visitN_layers(self)
            else:
                return visitor.visitChildren(self)




    def n_layers(self):

        localctx = TimelyParser.N_layersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_n_layers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Batch_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_batch_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBatch_size" ):
                listener.enterBatch_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBatch_size" ):
                listener.exitBatch_size(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBatch_size" ):
                return visitor.visitBatch_size(self)
            else:
                return visitor.visitChildren(self)




    def batch_size(self):

        localctx = TimelyParser.Batch_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_batch_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class N_epochsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_n_epochs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN_epochs" ):
                listener.enterN_epochs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN_epochs" ):
                listener.exitN_epochs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_epochs" ):
                return visitor.visitN_epochs(self)
            else:
                return visitor.visitChildren(self)




    def n_epochs(self):

        localctx = TimelyParser.N_epochsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_n_epochs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Drop_outContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(TimelyParser.FLOAT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_drop_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrop_out" ):
                listener.enterDrop_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrop_out" ):
                listener.exitDrop_out(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrop_out" ):
                return visitor.visitDrop_out(self)
            else:
                return visitor.visitChildren(self)




    def drop_out(self):

        localctx = TimelyParser.Drop_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_drop_out)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(TimelyParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lstm_neuronsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_lstm_neurons

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLstm_neurons" ):
                listener.enterLstm_neurons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLstm_neurons" ):
                listener.exitLstm_neurons(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLstm_neurons" ):
                return visitor.visitLstm_neurons(self)
            else:
                return visitor.visitChildren(self)




    def lstm_neurons(self):

        localctx = TimelyParser.Lstm_neuronsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_lstm_neurons)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptimizerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_optimizer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimizer" ):
                listener.enterOptimizer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimizer" ):
                listener.exitOptimizer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptimizer" ):
                return visitor.visitOptimizer(self)
            else:
                return visitor.visitChildren(self)




    def optimizer(self):

        localctx = TimelyParser.OptimizerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_optimizer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LossContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TimelyParser.STRING, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_loss

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoss" ):
                listener.enterLoss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoss" ):
                listener.exitLoss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoss" ):
                return visitor.visitLoss(self)
            else:
                return visitor.visitChildren(self)




    def loss(self):

        localctx = TimelyParser.LossContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_loss)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(TimelyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seq_lengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_seq_length

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq_length" ):
                listener.enterSeq_length(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq_length" ):
                listener.exitSeq_length(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq_length" ):
                return visitor.visitSeq_length(self)
            else:
                return visitor.visitChildren(self)




    def seq_length(self):

        localctx = TimelyParser.Seq_lengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_seq_length)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(TimelyParser.INT)
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
        self.enterRule(localctx, 92, self.RULE_p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
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
        self.enterRule(localctx, 94, self.RULE_q)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
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
        self.enterRule(localctx, 96, self.RULE_d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
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
        self.enterRule(localctx, 98, self.RULE_ps)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
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
        self.enterRule(localctx, 100, self.RULE_qs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
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
        self.enterRule(localctx, 102, self.RULE_ds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TimelyParser.INT, 0)

        def getRuleIndex(self):
            return TimelyParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = TimelyParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(TimelyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





