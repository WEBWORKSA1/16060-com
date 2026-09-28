/* =====================================================================
   16060.com — SITE CONFIG  (edit this file only to switch on revenue)
   ===================================================================== */
window.SITE = {
  name: "16060",
  domain: "16060.com",
  // Inquiry link shown on the top bar of every page
  inquiryUrl: "https://web.works/contact",

  // Contact routing — encoded so the address never appears in page source.
  // (Do not replace with a plain address.)
  _r: [96, 88, 101, 45, 120, 79, 108, 41, 118, 12, 71, 61, 122, 92, 110, 54, 57, 94, 104, 55],
  _k: [23, 61, 7, 90],

  // Form backend (static-host friendly). After the first submission,
  // FormSubmit emails an activation link — click it once.
  // Optional: replace with the random alias FormSubmit gives you.
  formAlias: "",

  // ---- Google AdSense -------------------------------------------------
  // Paste your publisher id (e.g. "ca-pub-1234567890123456") to go live.
  // Leave empty and house ads ("Advertise here") are shown instead.
  adsenseClient: "",
  adSlots: { top: "", inContent: "", sidebar: "", footer: "" },

  // ---- Analytics (optional) -------------------------------------------
  ga4: "",

  // ---- Donations --------------------------------------------------------
  currency: "USD",
  paypalEnabled: true,         // PayPal donate / subscribe buttons
  stripeLinks: {},             // e.g. { "18": "https://buy.stripe.com/..." }
  buyMeACoffee: "",            // e.g. "https://buymeacoffee.com/yourname"
  fundGoal: 6060,              // monthly operations goal (USD)
  fundRaised: 0,               // update manually as support arrives
  supporters: [],              // e.g. [{name:"Lin", amount:18, msg:"一路顺风!"}]

  // ---- Contest ------------------------------------------------------------
  contestDeadline: "2027-01-31T23:59:59-05:00",

  // ---- YouTube ------------------------------------------------------------
  // Add your own channel's video IDs first to earn from views.
  youtubeChannel: "",
  videos: [
    { id: "Kxg0_EpOcWs", title: "The Chinese zodiac, explained", tag: "Zodiac" },
    { id: "may2s9j4RLk", title: "The myth behind the Chinese zodiac", tag: "Zodiac" },
    { id: "pT52hREAf18", title: "Chinese lucky numbers", tag: "Numbers" },
    { id: "wf13M4MoHS4", title: "Chinese lucky and unlucky numbers explained", tag: "Numbers" },
    { id: "OAtBLAL2qZQ", title: "Why is 8 lucky, 4 unlucky and 9 romantic?", tag: "Numbers" },
    { id: "jEwbYNyHTzw", title: "The Chinese Zodiac explained", tag: "Culture" },
    { id: "A9JfsKmWpuE", title: "The Great Race: story of the Chinese zodiac", tag: "Stories" },
    { id: "SgyzVKYI6IY", title: "Chinese zodiac — a quick introduction", tag: "Zodiac" }
  ]
};
