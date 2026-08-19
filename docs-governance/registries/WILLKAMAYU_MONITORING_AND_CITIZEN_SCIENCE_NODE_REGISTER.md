# Willkamayu — Monitoring and Citizen-Science Node Register

Status: ACTIVE / DISCOVERY / PROPOSED NETWORK
Recorded: 2026-08-19
Owner: Converging Waters monitoring + citizen-science workstream

## Purpose and authority boundary

This register is the primary home for the **candidate monitoring-node architecture** and its connection to the emerging school/citizen-science network.

It does not finalize the MRV network, benefit geography, school roster, partner commitments or sensor procurement.

Authority split:
- `WILLKAMAYU_HYDROLOGY_AND_EVIDENCE_REGISTER.md` remains the primary home for hydrology, source history, water-quality evidence and source confidence.
- the school-research workstream remains the primary home for school counts, enrollment estimates and school-level verification;
- this register owns the **mapping between river segments / tributaries / candidate monitoring nodes and future citizen-science participation nodes**.

The 2026-08-19 update integrates a cross-conversation school-research synthesis supplied by Felipe. Source-derived ideas from that synthesis are recorded here only where they are either independently verified or clearly labeled as candidate architecture.

## Current candidate first corridor — NOT YET A COMMITMENT

Website-level orientation chain:

`Pisac → Calca → Huarán → Urubamba → Yanahuara → Pachar → Ollantaytambo`

Rules:
- these are orientation and participation nodes, not automatically permanent stations;
- measurement geography can extend outside the benefit corridor when source attribution requires it;
- station placement must later consider tributaries/discharges, hydromorphology, access, seasonality, sampling protocol and community priorities;
- the team must still decide final benefit geography and whether Cusco/Huatanay participates in Phase 1 or Phase 2.

## Verified node facts relevant to monitoring design

### Yanahuara

- Yanahuara is an officially recognized **centro poblado** in the district/province of Urubamba, with its own municipalidad de centro poblado.
- institutional and research sources recognize a **microcuenca Yanahuara** and a watercourse associated with Yanahuara that drains to the Urubamba/Vilcanota system.
- implication: Yanahuara should be treated as a distinct monitoring/citizen-science node rather than being collapsed into Urubamba city.

Sources:
- Municipalidad Provincial de Urubamba, Yanahuara centro poblado / municipal authorities: https://www.gob.pe/institucion/muniurubamba/noticias/905203-nuevas-autoridades-en-el-centro-poblado-de-yanahuara
- ANA indexed material referencing `Microcuenca Yanahuara`: https://www.ana.gob.pe/sites/default/files/normatividad/files/58-RD-0349-2019-03.pdf
- CIES study of microcuencas Qochoq–Calca and Yanahuara–Urubamba: https://cies.org.pe/investigacion/valoracion-economica-del-servicio-de/

### Pachar / Hatun Mayu

- Gobierno Regional Cusco describes the **subcuenca Hatun Mayu** as extending from the Poroy area to its **confluence with the Vilcanota in the sector of Pachar, district of Ollantaytambo**.
- implication: Pachar is not just another settlement node; it is a strategic tributary-confluence node carrying a second sub-basin signal into the main stem.
- ANA technical acceptance documentation lists **PGIRH-067 Pachar** as an **EHA — estación hidrológica automática**. The current evidence supports calling it a hydrological station; it must not be presented as a water-quality station unless the installed variables are separately verified.

Sources:
- Gobierno Regional Cusco, Hatun Mayu sub-basin to Pachar confluence: https://www.gob.pe/institucion/regioncusco/noticias/501018-en-el-marco-de-la-implementacion-del-acuerdo-regional-n-066-2021-cr-gr-cusco
- ANA, Informe Técnico N° 0028-2023-ANA-MGRH-CH, station list: `PGIRH-067 Pachar — EHA`: https://www.ana.gob.pe/sites/default/files/normatividad/files/INFORME%20TECNICO%20N%C2%B0%200028-2023-ANA-MGRH-CH.pdf

### Ollantaytambo / Patacancha

- the Patacancha river flows through the Patacancha/Huilloc system to Ollantaytambo and joins the Urubamba there.
- implication: a single main-stem measurement after Ollantaytambo would combine urban/town effects with the Patacancha tributary signal; attribution requires a finer design.

Sources:
- Municipalidad Distrital de Ollantaytambo tourism site, Huilloc/Patacancha description: https://ollantaytambodestinoseguro.muniollantaytambo.gob.pe/comunidad-de-huilloc/
- municipal Ollantaytambo site describing the town near the Patakancha–Urubamba confluence: https://ollantaytambodestinoseguro.muniollantaytambo.gob.pe/parque-arqueologico-de-ollantaytambo/

## Candidate diagnostic attribution architecture

This is a scoping hypothesis, not a finalized MRV design.

### HUA — Huambutío / Huatanay

- `M1` — main stem before receiving the Huatanay.
- `M2` — Huatanay immediately before confluence.
- `M3` — main stem immediately below Huambutío after mixing.

Purpose: distinguish upstream main-stem conditions from the Cusco/Huatanay contribution.

### YAN — Yanahuara

- `YAN-0` — Willkamayu / Vilcanota–Urubamba before the Yanahuara node/confluence.
- `YAN-T` — Yanahuara tributary before entering the main stem.
- `YAN-1` — main stem after mixing.

Purpose: measure the specific contribution of the Yanahuara microcuenca and keep Yanahuara analytically distinct from Urubamba.

### PACH — Pachar / Hatun Mayu

- `PACH-0` — main stem immediately before receiving Hatun Mayu.
- `PACH-HAT` — Hatun Mayu immediately before confluence.
- `PACH-1` — main stem downstream after mixing.

Purpose: estimate the contribution of a second sub-basin entering at Pachar.

Existing-infrastructure question:
- locate PGIRH-067 precisely;
- determine variables, data frequency, operational status and SNIRH accessibility;
- test whether Converging Waters/WGA should complement rather than duplicate ANA infrastructure.

### OLL / PAT — Ollantaytambo / Patacancha

- `OLL-0` — main stem before Ollantaytambo / before combined local influence.
- `PAT-0` — Patacancha before the urban area.
- `PAT-1` — Patacancha after traversing the town and before its confluence with the main stem.
- `OLL-1` — main stem just downstream of Ollantaytambo and the Patacancha confluence.

Purpose:
- compare Patacancha before/after the urban passage;
- distinguish tributary effects from the final combined downstream signal;
- use `OLL-1` as a candidate **outlet station for the first corridor**, enabling the question: what water condition entered the studied Sacred Valley corridor and what condition leaves it after Ollantaytambo?

## Sensor vs sampling rule

The architecture above does **not** imply a permanent sensor at every code.

Candidate operating model:
- recurrent main-stem reference stations where continuity matters;
- periodic tributary sampling where attribution matters;
- school/community sampling at selected nodes where protocol, safety and data quality allow it;
- portable/field instruments used where they add value without duplicating existing institutional infrastructure.

Final instrumentation belongs to later technical design with WGA and the team.

## Citizen-science school-network integration

The school-research synthesis suggests that a district-only school inventory is insufficient for basin citizen science.

Canonical mapping schema for the school workstream:

`district → populated center / microcuenca → school → students → nearest monitoring node / river question`

Examples to preserve for future design:
- Urubamba district → Urubamba;
- Urubamba district → **Yanahuara**;
- Ollantaytambo district → **Pachar**;
- Ollantaytambo district → Ollantaytambo;
- Ollantaytambo district → Patacancha-basin communities;
- Calca district → Calca;
- Calca district → Arín / Huarán.

The citizen-science network can therefore be understood as two superposed layers:

1. **Longitudinal Willkamayu network** — schools/communities distributed along the main-stem corridor.
2. **Diagnostic tributary network** — schools/communities associated with tributaries and microcuencas that enter the main stem.

A fuller longitudinal school-research chain may include nodes such as Coya, Lamay, Huayllabamba/Yucay and others even when the public website uses a sparser orientation chain. School-network density and website narrative density are different design questions.

### Huarocondo satellite hypothesis

Because Hatun Mayu drains a wider sub-basin before reaching Pachar, **Huarocondo is a candidate satellite citizen-science node**, not part of the current first-corridor commitment.

Possible future question: identify Huarocondo schools and perhaps 1–2 strategically located schools farther upstream in the Hatun Mayu system so students in that tributary can study the water that ultimately enters the Willkamayu at Pachar.

Do not expand the full school census into Poroy/Anta/Huarocondo until the team decides whether that satellite branch materially improves the first citizen-science design.

## Website-use rule

For `#system`, keep only enough detail to make the monitoring logic legible:
- one shared Huambutío confluence;
- proposed corridor including Yanahuara and Pachar;
- three diagnostic tributary nodes: Yanahuara, Pachar/Hatun Mayu, Ollantaytambo/Patacancha;
- distinction between benefit geography and measurement geography;
- downstream continuity as implication, not project footprint.

Do not turn `#system` into the school inventory.

When `#citizen-science` is explicitly reviewed in a future website delta, that section is the primary home for the school-network logic and the question-based participation model.

## Open decisions / research backlog

1. Verify the exact Yanahuara tributary/confluence geometry and candidate safe-access points.
2. Locate PGIRH-067 Pachar coordinates and current data feed; distinguish hydrological variables from water-quality variables.
3. Map Hatun Mayu tributary stations and candidate school nodes, including the Huarocondo satellite option.
4. Map Patacancha before-town / after-town / confluence access points and determine how much of Ollantaytambo's urban impact is carried through Patacancha versus direct main-stem discharges.
5. Define candidate post-Ollantaytambo `OLL-1` location far enough downstream for a meaningful mixed signal while preserving attribution value.
6. Integrate the verified school census from the school-research workstream into the schema `district → node → schools → students → monitoring question`.
7. Decide which points need continuous sensing, recurrent professional sampling, periodic citizen-science sampling or a combination.
8. Preserve all of the above as PROPOSED until team/territorial validation.
