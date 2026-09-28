/* Chinese festival dates 2025-2033 (computed from the lunisolar calendar) */
(function(){var M=[
[
"Lunar New Year",
"春节",
"The biggest festival of the year — family reunions, red envelopes, lion dances and fireworks.",
"1/1",
"2025-01-29 2026-02-17 2027-02-06 2028-01-26 2029-02-13 2030-02-03 2031-01-23 2032-02-11"
],
[
"Lantern Festival",
"元宵节",
"The first full moon closes the New Year season with lanterns, riddles and sweet tangyuan.",
"1/15",
"2025-02-12 2026-03-03 2027-02-20 2028-02-09 2029-02-27 2030-02-17 2031-02-06 2032-02-25"
],
[
"Qingming (Tomb-Sweeping Day)",
"清明节",
"Families sweep ancestors' tombs and enjoy spring outings.",
"solar term",
"2025-04-04 2026-04-05 2027-04-05 2028-04-04 2029-04-04 2030-04-05 2031-04-05 2032-04-04"
],
[
"Dragon Boat Festival",
"端午节",
"Dragon boat races and zongzi rice dumplings honour the poet Qu Yuan.",
"5/5",
"2025-05-31 2026-06-19 2027-06-09 2028-05-28 2029-06-16 2030-06-05 2031-06-24 2032-06-12"
],
[
"Qixi (Chinese Valentine's Day)",
"七夕",
"The legend of the Cowherd and the Weaver Girl, reunited once a year on a bridge of magpies.",
"7/7",
"2025-08-29 2026-08-19 2027-08-08 2028-08-26 2029-08-16 2030-08-05 2031-08-24 2032-08-12"
],
[
"Ghost Festival",
"中元节",
"Offerings are made to ancestors and wandering spirits in the middle of the 7th lunar month.",
"7/15",
"2025-09-06 2026-08-27 2027-08-16 2028-09-03 2029-08-24 2030-08-13 2031-09-01 2032-08-20"
],
[
"Mid-Autumn Festival",
"中秋节",
"Mooncakes, lanterns and moon-gazing under the fullest moon of the year.",
"8/15",
"2025-10-06 2026-09-25 2027-09-15 2028-10-03 2029-09-22 2030-09-12 2031-10-01 2032-09-19"
],
[
"Double Ninth Festival",
"重阳节",
"A day for climbing heights, chrysanthemums and honouring elders.",
"9/9",
"2025-10-29 2026-10-18 2027-10-08 2028-10-26 2029-10-16 2030-10-05 2031-10-24 2032-10-12"
],
[
"Winter Solstice Festival",
"冬至",
"'Winter solstice is as big as the New Year' — dumplings in the north, tangyuan in the south.",
"solar term",
"2025-12-21 2026-12-22 2027-12-22 2028-12-21 2029-12-21 2030-12-22 2031-12-22 2032-12-21"
],
[
"Laba Festival",
"腊八节",
"Laba congee marks the countdown to the New Year.",
"12/8",
"2026-01-26 2027-01-15 2028-01-04 2029-01-22 2030-01-11 2031-01-01 2032-01-20 2033-01-08"
]
];
var F=[];M.forEach(function(m){m[4].split(' ').forEach(function(d){F.push({name:m[0],zh:m[1],date:d,desc:m[2],lunar:m[3]})})});
F.sort(function(a,b){return a.date<b.date?-1:a.date>b.date?1:0});window.FESTIVALS=F;})();
