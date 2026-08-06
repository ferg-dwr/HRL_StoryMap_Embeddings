# HRL StoryMap — Panel Content, Media & To-Dos

**Project:** Healthy Rivers and Landscapes public StoryMap
**Platform:** ArcGIS StoryMaps → CNRA website (possibly 30x30 California)
**Audience:** General public, elementary reading level
**Last updated:** 2026-08-05

**Status key:** ✅ drafted · 🟡 partial · ⬜ not started

---

## Standing conventions

- **Every screen is a Sidecar (docked). Every slide within it is a Panel.**
  No Slideshow blocks, no standalone blocks. One vocabulary applies throughout.
- **Bold** on first use = vocabulary term. Definition card at
  `https://ferg-dwr.github.io/HRL_StoryMap_Embeddings/words/<slug>.html`
- **Elementary US reading level throughout.** Short sentences, one idea each. If a word
  can't be avoided, it gets bolded and gets a card — no exceptions
- **Voice: SciShow / Crash Course.** Curious, direct, a little wry. Talk *to* the reader.
  Ask the question they're already thinking, then answer it
- **Banned construction:** "It's not X, it's Y." Say Y
- **Keep it tight.** Cut any sentence that repeats the one before it
- Every panel answers a question the previous panel made the reader ask
- No number lands before the reader has a reason to care about it

## Media conventions

Each panel lists one **primary media** for the Sidecar stage. Three sourcing categories:

| Tag | Meaning |
|---|---|
| **DWR** | Request from DWR photo/video library — specific ask written out |
| **MAP** | ArcGIS web map, hosted by us |
| **FIG** | Custom figure — notebook-generated PNG, or interactive HTML on GitHub Pages |

Interactive figures use the same GitHub Pages repo as the vocabulary cards
(`HRL_StoryMap_Embeddings`), embedded as iframes. Marked **FIG-i** below.

---

# CHAPTER 1 — The Delta We Had

## Screen 1 · Meet the watershed

**Format:** Sidecar (docked) · 5 panels
**Status:** ✅ copy drafted · 🟡 media in progress

### Panel 1 — It all starts in rivers and streams, far from the ocean ✅

> Winter in California - in wet years, it's raining, and high up in the Sierra Nevada mountains, it's snowing.
>
> When spring comes, the rivers rise with snow melt. And melted snow does what all water does — it runs downhill.
>
> It starts in tiny streams you could step across. Those streams join up and get bigger. They become rivers with names: the Yuba. The American. The Tuolumne.
>
> All of them are heading for the same place - the lower watershed, then the ocean.
>
> But it isn't just the water moving downstream. Baby salmon are on the move too, starting their journey to the ocean.

**Media — MAP:** Statewide map on light gray canvas. Sierra extent, then headwater
streams, then named tributaries revealed across panels 1–2 via per-panel layer
visibility. Globe inset (static PNG) bottom corner.

**Alternate / addition — DWR:** *If available* — footage or stills from a **DWR snow
survey at Phillips Station**. Surveyors in the snow with the measuring tube is one of
the most recognizable images in California water, it is unmistakably DWR, and it opens
the story with people rather than a diagram. Strong candidate for an autoplay video
panel.

### Panel 2 — Everything funnels to one spot ✅

> Those rivers feed into two big ones. The Sacramento River flows down from the north. The San Joaquin River flows up from the south.
>
> Together, they drain almost half of California. Rain and snowmelt from an enormous stretch of the state — mountains, foothills, farmland, towns — all of it drains into these two rivers.
>
> And the two rivers meet in one place, right in the middle of the state. Then they head west toward the ocean.
>
> That meeting place is called the **Delta**. Almost every drop of water in this story passes through it. And so must all the salmon born upstream in these rivers - they too must travel through the Delta to arrive at the ocean.

**Media — MAP:** Same web map, zoomed to the confluence, Sac–SJ watershed boundary
shaded. The shaded polygon *is* the "almost half of California" claim — show it rather
than assert it.

### Panel 3 — A place that was mostly water ✅

> If you could visit the Delta 200 years ago, you might have trouble finding a place to stand.
>
> Most of it was marsh — soft, wet ground covered in tall green reeds called **tule** (say: TOO-lee). Some tule grew taller than a basketball hoop.
>
> Every spring, all that mountain snow arrived at once. The rivers filled up and spilled out sideways. Water spread across hundreds of thousands of acres, shallow and slow and warm in the sunlight.
>
> Then it drained away again. And the marsh soaked up what was left, like a giant sponge.

**Media — DWR:** *If available* — a **ground-level photo of tule marsh**, ideally with a
person or boat for scale so "taller than a basketball hoop" lands. Restoration sites
(Prospect Island, Lower Elkhorn Basin, Yolo Bypass margins) likely have usable imagery.
**Fallback:** historical illustration or painting of the pre-1900 Delta; or the SFEI
historical layer alone.

### Panel 4 — And it was crowded ✅

> All that shallow, sunny water grew food. Tiny plants. Tiny bugs. Billions of them.
>
> So everything came to eat. Millions of ducks and geese stopped here on their way south for winter. Beavers, river otters, and elk lived in the marsh.
>
> And every year, young salmon came down out of those same mountain streams where the snow melts — and stopped here, in the Delta, to eat and grow before heading out to sea.

*Closes the loop back to Panel 1 and plants salmon before Screen 4 needs them.*

**Media — DWR:** *If available* — **waterfowl on a flooded field**, Delta or Yolo Bypass.
Migratory birds on winter-flooded rice ground is a strong, common Central Valley image
and it quietly previews Chapter 2's farming-and-habitat argument.
**Alternate — MAP:** Pacific Flyway overlay showing the Delta as a stopover.

### Panel 5 — The Delta...✅

> ... was a **kitchen**. Shallow, sunny water grew food, and that food fed everything else. This includes people, from time immemorial, from the first Indigenous people, who came to the Delta to fish for salmon and other species, and to harvest the tule and other plants for baskets and housing.
>
> ... was a **sponge**. When the rivers ran high, the **marsh** spread that water out and slowed it down.
>
> ... was a **nursery**. Young salmon grew bigger and stronger here before facing the ocean.
>
> The Delta did all of this for thousands of years. 

**Three jobs — kitchen, sponge, nursery — are the spine of Chapter 1.** Screen 3 pays
off each one by name.

**Media — FIG-i:** *Recommended interactive.* Three-panel figure, one per job, where
hovering or tapping a job highlights it and dims the others. Simple SVG + a little JS,
same GitHub Pages repo. Low effort, and it makes the three jobs stick — which matters,
because the entire Screen 3 structure depends on the reader remembering them.
**Fallback — FIG:** static 3-icon graphic.

### Screen 1 to-dos
- [ ] Confirm tributary names match HRL project rivers (program office)
- [ ] Confirm "almost half of California" vs. published ~40% figure
- [ ] Build tributary reveal layers in AGOL (one filtered copy per river)
- [ ] **Request from DWR:** snow survey footage/stills (Phillips Station)
- [ ] **Request from DWR:** tule marsh ground-level photo with scale reference
- [ ] **Request from DWR:** waterfowl on flooded Delta or bypass field
- [ ] Build three-jobs interactive (FIG-i)
- [ ] Decide: globe inset static PNG vs. interactive treatment
- [ ] Alt text for all media

---

## Screen 2 · What we changed

**Format:** Sidecar (docked) · 6 panels
**Status:** ✅ copy drafted · 🟡 media partial
**Note:** Swipe comes *before* the numbers — feel first, count second.

### Panel 1 — Setup ✅

> The Delta you just saw — the marsh, the tule, the shallow water spreading out every spring — is mostly gone.
>
> Most of it disappeared in about a hundred years.
>
> Here's what it looked like before, and what it looks like now.

**Media — DWR:** *If available* — a **wide aerial of the modern Delta**, showing straight
channels and geometric fields. Sets up the contrast before either map appears.

### Panel 2 — The 1800s map ✅

> This is the Delta around 1800, before the changes began.
>
> The green and blue is wet ground — marsh, ponds, and channels that filled and drained with the seasons. Look how much of it there is. Look how the water wanders.
>
> This is what a river system looks like when nobody has told it where to go. For a baby salmon, looking to eat, hide, rest, and move its way downstream, this version of the Delta would offer options for feeding, bolstering itself for the big ocean waters ahead.

**Media — MAP:** ✅ **Published.** SFEI 1800s floodplain / habitat map.

*Caption: Historical Delta habitats, mapped by the San Francisco Estuary Institute from survey records, ships' logs, and land grant documents from the 1800s.*
*Source: https://www.sfei.org/projects/sacramento-valley-historical-ecology*

### Panel 3 — What changed ✅

> So what happened?
>
> Civilization grew, more people arrived, and they saw something different than we see now. They saw rich soil under all that water — some of the best farmland anywhere in the world, if only it could be drained.
>
> So they drained it. They built **levees**, long walls of earth, to hold the rivers in place. They dug channels to carry the water away. They turned marsh into fields.
>
> And it worked. The Delta became farmland that feeds people across the country. Towns grew. Highways crossed it. Water from these rivers now travels hundreds of miles to homes and farms all over California.
>
> Call it a trade. People got farmland, cities, and a water supply. What they gave up was harder to see, and it took a long time to notice.

*Framing note: "trade, not crime" is what lets farmers and water agencies stay in the
story through Chapter 2.*

**Media — DWR (archival):** *If available* — a **historical photograph of Delta
reclamation**: clamshell dredge, levee construction, or a crew building embankments.
This is the single highest-value photo request in the project. A real photo of people
doing the work makes the trade concrete in a way no map can, and it puts human faces on
a decision the story is asking readers to understand rather than condemn.
**Fallback:** State Library / UC archives; check rights before use.

### Panel 4 — The 2012 map ✅

> This is the same place today.
>
> The wet ground is nearly gone. What's left is mostly straight lines — channels that go where we sent them, fields where the marsh used to be.
>
> The Delta is still here. But it's a different kind of place now.

**Media — MAP:** ✅ **Published.** USGS 2012 land cover map.

*Caption: Delta land cover in 2012, U.S. Geological Survey.*

### Panel 5 — The swipe ✅

> Drag the slider back and forth.
>
> One side is 1800. The other side is today.
>
> Watch the green go away.

**Media — MAP:** Swipe block, SFEI 1800s vs. USGS 2012. Both layers already published —
this needs assembling, not sourcing.

### Panel 6 — The numbers ✅

> The Delta has lost about **86%** of its floodplain. [_check #s - see LC comment - some articles report >90% loss, and Cloern et al. 2021 say 76% loss - it all depends on the spatial scale measured and whether the analysis is counting floodplains, wetlands, or both. Maybe we move away from a single number and put a "greater than" prefix of say a range?]_
>
> About 706,000 acres of floodplain and wetland have become roughly 98,000. That's a little over 600,000 acres gone — [SIZE COMPARISON TBD].
>
> And the marsh didn't take its jobs with it. The kitchen, the sponge, the nursery — those jobs are now only getting done at fraction of what they were originally.

**Media — FIG:** Floodplain loss figure from `Delta_Floodplain_Analysis.ipynb`.
**Consider FIG-i:** an animated or draggable bar that shows 706,000 shrinking to 98,000.
Watching the number fall beats reading it.

### Screen 2 to-dos
- [ ] **Verify acreage against `Delta_Floodplain_Analysis.ipynb`** — 706,000 → 98,000
- [ ] **Pick size comparison.** Rhode Island (~776,000 ac) is larger than the loss —
      soften the wording or find a California comparison that lands precisely
- [ ] **Request from DWR:** wide aerial of modern Delta
- [ ] **Request from DWR / archives:** historical reclamation photo (highest priority)
- [ ] Confirm SFEI attribution and permission for map use
- [ ] Confirm USGS 2012 dataset citation format
- [ ] Build swipe block from the two published layers
- [ ] Decide whether one extra sentence explains *how* the 1800s map was reconstructed

---

## Screen 3 · Consequences

**Format:** Sidecar (docked) · 5 panels
**Status:** ✅ redrafted — needs review
**Structure:** three beats matching the three jobs from Screen 1 Panel 5. Practical
stakes folded into each. Human relationship — tribal, historical, recreational — stays
on Screen 8.

**Layout note:** "Why it matters to you" was designed for full page width. Inside a
docked sidecar panel it needs a distinct visual treatment so it reads as an aside rather
than more body text. Options: a short rule above it plus bold lead-in, or a small
FIG-i embed styled like the vocabulary cards. Recommend the latter for consistency.

### Panel 1 — Opening

> When the marsh disappeared, the Delta stopped doing its jobs.

**Media — FIG-i:** Reprise the three-jobs interactive from Screen 1 Panel 5, now with
each job greyed out or marked. Reusing the same graphic makes the callback visual as
well as verbal.

### Panel 2 — The kitchen closed

> Shallow water that sits in the sun makes food. Sunlight reaches the bottom. Tiny plants grow. Tiny bugs eat the plants. Fish eat the bugs.
>
> Deep, straight **channels** work differently. The water moves too fast. Sunlight stops partway down. Not much grows.
>
> Scientists tested this right here in the Central Valley. Just west of Sacramento there is a wide, flat piece of farmland called the **Yolo Bypass**. It is built to flood on purpose. Young salmon that spent a few weeks on those flooded fields grew faster than salmon that stayed in the river.

> **But why should we care?**
>
> The Yolo Bypass was built to keep Sacramento from flooding. When the river runs high, the water spreads out there instead of into the city. The same flooded field that feeds baby salmon is the one keeping neighborhoods dry — and farmers grow rice on it the rest of the year.

**Media — DWR:** Pascale suggestion on animation of flooding as seen by satellite imagery.

**Supporting — FIG:** food web comparison, shallow floodplain vs. deep channel. _consider a picture comparison of salmon raised in the floodplain vs the river and the food web between the two_

### Panel 3 — The sponge dried out

> **Marsh** soil is strange stuff. It is made of dead plants that piled up underwater for thousands of years. Underwater, plants rot very slowly, so the pile just kept growing. This soil is called **peat**, and it holds water like a sponge.
>
> When people drained the marsh, air reached that soil for the first time. And the peat started to disappear. Slowly, quietly, it turned into gas and floated away.
>
> As it disappeared, the land sank.
>
> Some Delta islands now sit lower than the water outside their **levees**. In places, two or three stories lower.

> **But why should we care?**
>
> Those levees protect farms, towns, highways, and the pipes that carry drinking water to millions of Californians. The land behind them keeps dropping. So the walls have to keep getting taller.

**Media — DWR:** *If available* — a **photo taken from atop a Delta levee** looking down
at the island below, with water visible on the other side. Nothing explains subsidence
faster than seeing a boat higher than a farm.
**Supporting — FIG-i:** cross-section showing land surface dropping below sea level over
time, with a year slider. Strong interactive candidate — the mechanism is temporal and a
static figure has to work hard to show it.

### Panel 4 — The nursery emptied out

> Young fish need shallow, slow water to grow up in. Places to hide. Enough food to get big fast.
>
> The Delta used to be full of those places. It was also full of **native** fish that live nowhere else on Earth. Sacramento perch. Delta smelt. Thicktail chub.
>
> The thicktail chub has not been seen since the 1950s. It is gone. A fish that lived only here, and now does not live anywhere.

> **But why should we care?**
>
> When native fish get into trouble, people feel it too. Salmon fishing has been closed in California in recent years. That hits fishing families, boat owners, and coastal towns. And rules made to protect fish in trouble shape how much water can be sent to farms and cities. Healthy fish make those choices easier for everyone.

**Media — FIG:** Native fish vignettes — illustrations or specimen photographs with
names. Consider CDFW as a source if DWR imagery is thin.

### Panel 5 — Closing, hinge into Screen 4

> One fish ties all of this together. It needs the mountains, the Delta, and the ocean. All of it. Every single generation.
>
> And its numbers have been falling for a hundred years.

**Media — DWR:** *If available* — a **single strong Chinook salmon image**. Underwater,
in hand during monitoring, or on a spawning gravel bed. Hands off to Screen 4.

### Screen 3 to-dos
- [ ] Confirm Yolo Bypass salmon growth finding and pick a citation
- [ ] Verify subsidence depths with a DWR data lead ("two or three stories")
- [ ] Confirm thicktail chub last-observed date
- [ ] **Decide whether to name Delta smelt** — politically loaded in CA water debate.
      Thicktail chub carries the emotional weight without the baggage
- [ ] Decide whether to name carbon/climate explicitly in Panel 3
- [ ] **Request from DWR:** Yolo Bypass flooded + dry aerial pair
- [ ] **Request from DWR:** levee-top photo showing subsided island
- [ ] **Request from DWR:** Chinook salmon hero image
- [ ] Build food web figure
- [ ] Build subsidence cross-section (FIG-i candidate)
- [ ] Source native fish vignettes (check CDFW)
- [ ] Decide and build the "Why it matters to you" treatment inside sidecar panels

---

## Screen 4 · Salmon in decline

**Format:** Sidecar (docked) · 5 panels
**Status:** ✅ drafted — numbers to be filled in

### Panel 1 — Why this fish

> Let's follow one fish.
>
> **Chinook** salmon (say: shi-NOOK) use the whole system. Mountains, rivers, Delta, ocean — every part of it, every generation. No other animal here depends on so many pieces working at once.
>
> Which makes them a pretty good alarm bell. When something breaks anywhere in the watershed, salmon are usually the first to tell us.

**Media — DWR:** *If available* — **adult Chinook on a spawning bed**, or a close portrait.

### Panel 2 — How do you count a fish?

> Fair question. Fish live underwater. They move around. You cannot line them up and count heads.
>
> Salmon solve this for us, because salmon come home. Every year the grown ones swim back up the same rivers where they hatched. So people go stand at those rivers and count the ones that make it.
>
> California has been doing this since the 1950s. Decades of people in waders, clipboards in hand, counting fish one at a time.

*Gets past "escapement" without ever using the word.*

**Media — DWR:** *If available* — **field crew counting or sampling fish**. Rotary screw
trap, weir, carcass survey, anything with people doing the work. This panel is quietly
about *how we know things*, which is the foundation of Chapter 2's credibility argument.
Showing real fieldwork here pays off later.

### Panel 3 — The graph

> These are the counts for fall-**run** Chinook. "Fall run" means the group that comes home in autumn, and it is the biggest group in the Central Valley — the one most people mean when they say salmon.
>
> Each point is one year. Higher means more fish made it home.

**Media — FIG-i:** *Strong interactive candidate.* Fall-run Chinook counts over time
from GrandTab. Hover a year to see the count; optionally toggle other runs on. A static
PNG works, but a time series is exactly the kind of figure where letting people poke at
individual years builds trust. Source: `Chinook_Escapement_Figure.ipynb`.

### Panel 4 — What it shows

> In [YEAR], about [NUMBER] fish came home.
>
> By [YEAR], that number was about [NUMBER].
>
> The line bounces around a lot, and that part is normal. Rain, ocean temperature, and food supply all swing from year to year, so salmon numbers swing too. Watch the overall shape rather than any single year.
>
> The shape goes down.

**Media:** Same figure, with the two cited years highlighted.

### Panel 5 — Why

> Now hold that graph next to the maps you just saw.
>
> The marsh drained. The floodplains got walled off. The kitchen closed, the sponge dried out, and the nursery emptied.
>
> Losing habitat is one of several problems. Dams block the cold upstream water where salmon lay eggs. Warm water kills those eggs. Ocean conditions swing hard. But every one of those problems gets worse when there is nowhere left for young fish to grow.

*"One of several problems" matters — a single-cause claim invites a fight from anyone
who studies this, and Chapter 2's credibility rests on Chapter 1 being careful.*

**Media — MAP:** Delta extent showing habitat loss and the salmon graph side by side, or
the swipe map reprised small.

### Screen 4 to-dos
- [ ] **Fill in years and counts** from GrandTab
- [ ] Resolve: fall run only, or all runs shown together?
- [ ] Build interactive escapement figure (FIG-i) from `Chinook_Escapement_Figure.ipynb`
- [ ] Confirm the 1950s start date for California salmon counting
- [ ] **Request from DWR:** fish monitoring fieldwork imagery
- [ ] Decide whether to name specific dams in Panel 5
- [ ] Alt text for the figure

---

## Screen 5 · The salmon lifecycle

**Format:** Sidecar (docked) · 4 panels (Panel 2 may split into 6 sub-panels)
**Status:** ✅ drafted · 🟡 map in progress
**Structural note:** ends Chapter 1 so watershed scope is established before Chapter 2.

### Panel 1 — The question

> So why does a drained marsh matter to a fish that spends most of its life in the ocean?
>
> Follow one salmon all the way through and you will see it.

**Media — MAP:** Full watershed extent, mountains to ocean. Establishing shot.

### Panel 2 — The journey

Consider splitting into six panels, one per stage, with the map advancing each time.
That is the single best use of a Sidecar in the whole story.

> **It starts in the mountains.** A salmon egg sits in clean **gravel** at the bottom of a cold stream, high up in a tributary. The egg hatches. The fish is smaller than your finger.
>
> **It heads downstream.** The young salmon rides the spring water down, out of the mountains, toward the middle of the state.
>
> **It stops in the Delta.** This is the part people miss. Young salmon do not race through the Delta. They stop, and they eat, and they grow — sometimes for weeks. And while they are here, their bodies rebuild to survive in salt water. Same fish, different plumbing.
>
> **It goes to sea.** Out through the Golden Gate and into the Pacific, where it spends two to four years growing into something twenty times its size.
>
> **It comes home.** Then it turns around and swims back — up the coast, through the Delta, up the rivers, and into the same stream where it hatched. Scientists think it navigates partly by smell.
>
> **It lays eggs, and it dies.** Its body stays in the river and feeds everything around it. Bears, birds, bugs, trees. Nutrients from the Pacific Ocean end up in a forest a hundred miles inland, carried there by fish.

**Media — MAP per stage:** the lifecycle map with the active stage highlighted and the
camera moving to that part of the watershed.
**Supporting — DWR:** *If available* — one photo per stage: eggs in gravel, juvenile in
hand or net, adult on the spawning bed, carcass in a stream. A photo-per-stage sequence
would make this the most memorable screen in the piece.

### Panel 3 — Why the Delta matters so much

> Look at where the Delta sits on this map.
>
> Every salmon passes through it twice. Once on the way out, small and hungry. Once on the way back, grown and heading home.
>
> A salmon that leaves the Delta bigger has a much better shot at surviving the ocean. So the size of a fish in spring shapes how many come home years later.
>
> That marsh was where the fish got big enough to make it.

**Media — MAP:** Zoom to the Delta with both migration directions drawn.

### Panel 4 — Where the journey breaks *(pending Scott's input)*

> [Placeholder — same map, trouble spots marked: blocked upstream habitat, warm water,
> missing floodplain, water diversions, predators in straight channels.]
>
> A salmon has to survive every single one of these. Miss one, and the journey ends.

**Media — FIG-i:** *Strong interactive candidate.* Lifecycle map with stressors as
clickable points; tapping one explains it in a sentence. This is Scott's figure content,
and interactivity handles the volume of information without overwhelming the panel.

### Screen 5 to-dos
- [ ] **Ask Scott** about showing stressors spatially
- [ ] Reference Figure 3 from the life-history diversity paper
- [ ] Decide: one journey panel or six
- [ ] Build lifecycle map with per-stage highlighting
- [ ] **Request from DWR:** lifecycle stage photos (eggs, juvenile, adult, carcass)
- [ ] Verify "two to four years" ocean residence for fall-run Chinook
- [ ] Verify "twenty times its size" growth figure
- [ ] Confirm the smell-based navigation claim is stated at the right confidence level
- [ ] Decide whether the carcass-nutrients beat stays — lovely, but is it a detour?
- [ ] Alt text for each map state

---

# CHAPTER 2 — Sharing the Water

*Merged from the former Chapters 2 and 3. The arc: what we built → who needs the water →
what it means to people → what HRL does → where → how we know it works → what's next.*

*Why the merge works: naming specific infrastructure makes competing demands concrete
instead of abstract, so HRL arrives as an answer to a question the reader can picture.
It also fixes the old structure's weakness — Chapter 2 used to end on obstacles and
deflate right before the payoff.*

## Screen 6 · What we built ⬜

**Format:** Sidecar (docked) · ~5 panels
**Status:** ⬜ copy not drafted
**Content:** The infrastructure, named and shown. Shasta. Oroville. Folsom. New Melones.
The pumping plants in the south Delta. The aqueducts. The Yolo Bypass (already met on
Screen 3). Why each was built, what it does, who it serves.

**Framing:** continue "trade, not crime." These are working systems that millions of
people depend on. Naming them plainly and showing their scale earns credibility with
water agencies and makes the competing-demand problem real rather than theoretical.

**Media — DWR:** This is DWR's home turf and the imagery almost certainly exists.
*If available* — **Oroville Dam and spillway**, **Banks Pumping Plant**, **the California
Aqueduct running through farmland**, **a reservoir at low water**. Aerials preferred;
scale is the point.
**Media — MAP:** infrastructure map — major reservoirs, aqueducts, pumping facilities,
with the watershed underneath.

## Screen 7 · Everyone needs the same water ⬜

**Format:** Sidecar (docked) · ~4 panels
**Status:** ⬜ copy not drafted
**Content:** Cities. Farms. Fish. Flood protection. Recreation. The same water, several
legitimate claims. Explain the Bay-Delta Water Quality Control Plan at elementary level
without wading into the politics. State the honest constraint: there is not enough to
give everyone everything, in most years.

**Media — FIG-i:** *Strong interactive candidate.* Where the water goes — a flow or
allocation diagram the reader can explore, ideally showing how it shifts between wet and
dry years. Static won't carry this; the whole point is that the answer changes.
**Media — DWR:** *If available* — paired images of the same reservoir in a wet year and
a drought year.

## Screen 8 · Salmon and people ⬜

**Format:** Sidecar (docked) · ~4 panels
**Status:** ⬜ copy not drafted — needs contributor input
**Content:** The emotional turn. Tribal relationships with salmon. Fishing families and
coastal communities. Historical significance. Modern life in the Delta. The argument
that people and salmon are not on opposite sides.

**Needs:** Anecita Agustinez (Tribal Policy Advisor) on tribal content and sign-off;
Mariko Falke on framing.

**Media — DWR / partner:** *If available and with appropriate permission* — imagery of
tribal fishing or ceremony **only with explicit consent and sign-off**. Otherwise
commercial and recreational fishing, Delta communities, people on the water.

## Screen 9 · The plan ⬜

**Format:** Sidecar (docked) · ~4 panels
**Status:** ⬜ copy not drafted
**Content:** HRL itself. Three plain ideas: **more water**, **more room to grow**,
**science that keeps checking**. What the program actually commits to and how flow plus
habitat work together rather than separately.

**Media — MAP:** HRL project boundaries across the watershed. Reinforces that this is a
whole-system program, not a Delta-only one.
**Media — DWR:** Secretary Crowfoot or Deputy Secretary Arthur video (script drafted;
outdoors; under a minute; muted autoplay so captions are required).

## Screen 10 · Where it's happening ⬜

**Format:** Map Tour — *the one exception to the all-Sidecar rule.* Real sites,
click-through, each with a photo and a sentence.
**Status:** ⬜
**Content:** Example projects — Prospect Island, Lower Elkhorn Basin, tributary work.
Plus "the people of HRL."

**Media — DWR:** *If available* — **before/after or during-construction photos** for each
project site. Construction imagery is persuasive precisely because it is unglamorous:
it shows work being done rather than promised.

## Screen 11 · How do we know it's working ⬜

**Format:** Sidecar (docked) · ~3 panels
**Status:** ⬜ copy not drafted
**Content:** The credibility beat. "We watch. We measure. We change what we do."
Monitoring, and what happens when results come back different than expected.
**Avoid the term "adaptive management"** — say what it means instead.

**Media — DWR:** *If available* — **monitoring in action**: crews with nets, screw traps,
water quality sondes, tagging. Callback to Screen 4 Panel 2 — same kind of work, now
pointed at the future rather than the past.
**Media — FIG-i:** if any early monitoring results exist and are cleared for release, an
honest chart beats any amount of description.

## Screen 12 · What comes next ⬜

**Format:** Sidecar (docked) · ~2 panels
**Status:** ⬜
**Content:** Forward-looking close. What the Delta could look like in thirty years if
this works. Sources and further reading move to a footer rather than being the ending.

**Media — DWR:** a hopeful image — restored habitat with water on it, or people in the
field. End on something living.

---

# Media inventory

## Already published ✅
- SFEI 1800s floodplain / habitat map (Screen 2 Panel 2)
- USGS 2012 land cover map (Screen 2 Panel 4)

## DWR requests — priority order
| # | Ask | Screen | Why it matters |
|---|---|---|---|
| 1 | Historical Delta reclamation photo (dredge / levee construction) | 2·3 | Makes "the trade" human; nothing else does this job |
| 2 | Yolo Bypass flooded + dry aerial pair | 3·2 | The whole floodplain argument in two frames |
| 3 | Snow survey at Phillips Station (video or stills) | 1·1 | Opens on people, unmistakably DWR |
| 4 | Levee-top photo showing subsided island | 3·3 | Explains subsidence instantly |
| 5 | Fish monitoring fieldwork | 4·2, 11 | Grounds the "how we know" argument twice |
| 6 | Chinook salmon hero image | 3·5, 4·1 | Chapter 1's emotional handoff |
| 7 | Infrastructure aerials (Oroville, Banks, Aqueduct) | 6 | Scale is the point |
| 8 | Lifecycle stage photos (eggs, juvenile, adult, carcass) | 5·2 | Would make Screen 5 the most memorable in the piece |
| 9 | Tule marsh at ground level, with scale | 1·3 | Sells "taller than a basketball hoop" |
| 10 | Waterfowl on flooded field | 1·4 | Previews the farming-and-habitat argument |
| 11 | Wide aerial of modern Delta | 2·1 | Sets up the contrast |
| 12 | Project before/after and construction photos | 10 | Unglamorous work is persuasive |
| 13 | Reservoir wet year vs. drought year pair | 7 | Shows variability without words |
| 14 | Restored habitat, hopeful closing image | 12 | End on something living |

## Custom figures — static (FIG)
- [ ] Three jobs graphic (kitchen / sponge / nursery) — Screen 1·5
- [ ] Floodplain loss figure — Screen 2·6 — *notebook exists*
- [ ] Food web comparison, floodplain vs. channel — Screen 3·2
- [ ] Native fish vignettes — Screen 3·4
- [ ] Lifecycle map with per-stage highlighting — Screen 5

## Custom figures — interactive (FIG-i)
Hosted in `HRL_StoryMap_Embeddings` alongside the vocabulary cards, embedded as iframes.

| Figure | Screen | Why interactive earns it |
|---|---|---|
| Three jobs, tap to highlight | 1·5, reprised 3·1 | Makes the spine of Chapter 1 stick |
| Escapement time series, hover for year | 4·3 | Poking at real years builds trust in the data |
| Lifecycle stressors, tap each point | 5·4 | Handles Scott's information volume without crowding |
| Subsidence cross-section with year slider | 3·3 | Mechanism is temporal; static has to work hard |
| Where the water goes, wet vs. dry year | 7 | The answer changes — that *is* the content |
| Acreage 706,000 → 98,000, animated | 2·6 | Watching a number fall beats reading it |

*Build order suggestion: three jobs first (smallest, and two screens depend on it), then
escapement, then lifecycle stressors.*

---

# Block format plan

Everything is a **Sidecar (docked)** except Screen 10, which is a **Map Tour** because
click-through place-by-place is exactly what that block is for.

Sidecars are immersive and take over the viewport. Twelve in a row is a lot of
controlled pacing, so watch panel counts — 4 to 6 panels per screen keeps momentum.
Anything longer should probably be two screens.

---

# Vocabulary status

**Live (25):** delta · watershed · tributary · snowpack · tule · floodplain · wetland ·
marsh · peat · channel · habitat · native · salmon · chinook · run · gravel · spawn ·
migrate · estuary · levee · sediment · ecology · ecosystem · restoration · monitoring

**Style sweep done:** "It's not X, it's Y" removed from wetland, estuary, restoration,
marsh, and floodplain cards, and from Screen 1 Panel 5, Screen 2 Panels 1–3, and
Screen 3 Panels 2–3.

**Words used but not yet carded — decide card vs. rewrite:**
- [ ] *Yolo Bypass* — proper noun, explained inline. Probably fine as is
- [ ] *escapement* — avoided entirely on Screen 4. Keep it that way
- [ ] *smolt* — deliberately not used. "Young salmon" instead
- [ ] *adaptive management* — Screen 11. Needs plain-language replacement, not a card
- [ ] *diversion* — will come up on Screens 6–7
- [ ] *reservoir* — Screen 6. Likely needs a card
- [ ] *aqueduct* — Screen 6. Likely needs a card
- [ ] *drought* — Screen 7. Probably known, but worth a card at this reading level

**Rule of thumb:** if a fourth grader would stop reading to ask what it means, it needs
a card. If a card can't make it clear in three sentences, rewrite the sentence instead.

---

# Cross-cutting to-dos

- [ ] Confirm HRL tributary list with program office
- [ ] Verify all acreage and percentage figures against notebooks
- [ ] Alt text for every figure, map, and photo (state accessibility requirement)
- [ ] Captions on the Crowfoot/Arthur video — StoryMaps autoplay is muted by default
- [ ] Identify draft reviewers and data leads
- [ ] CNRA communications review of the Secretary video script
- [ ] Confirm Prospect Island (1,600 ac) and Lower Elkhorn Basin (1,000 ac) acreages
- [ ] Bay-Delta Plan adoption status — keep language evergreen until confirmed
- [ ] Tribal content sign-off before publication
- [ ] Decide embed vs. link vs. inline for each vocabulary term
- [ ] Photo rights and attribution check on every non-DWR image
