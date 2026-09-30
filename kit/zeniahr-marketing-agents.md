# ZeniaHR Social & Performance Marketing: Agent Team

ZeniaHR only (Instagram @zenia_hr + LinkedIn page "ZeniaHr"). Pulpit Mobility is a separate brand and is out of scope.

Zoho Social (MCP server `socialzeniahr`): portal_id 60087141507, brand_id 483774000000012072. Channels: linkedinpage, instagram. Never post to X/Twitter.

Source docs in the ZENIAHR project: `claude/zeniahr-content-calendar.md` (what to post), `claude/zeniahr-design-kit.md` (how it looks).

## The team

| Agent | Runs | Job | Output |
|---|---|---|---|
| 1. Strategist & Copywriter | Weekly, Sunday | Plans next Mon–Sun from the calendar, checks EPFO/ESIC/labour news, writes captions | Week brief: topic, template, ground (k), IG caption (Hinglish), LinkedIn caption (English), hashtags |
| 2. Creative Designer | Weekly, Sunday (after 1) | Renders the week's posts with the design kit: statics, carousels, 2 motion posts | PNG/JPG + MP4/GIF, public URLs, manifest |
| 3. Publisher & Community | Weekly schedule + daily check | Schedules the week in Zoho Social; daily: failed posts, new comments/DMs, drafts replies | Scheduled posts; daily digest of comments with suggested replies |
| 4. Performance Analyst | Weekly, Monday | Reads last 7/28 days of results, picks winners, feeds learnings back to agent 1 | Weekly report: reach, engagement rate, saves/shares, best template/topic, next-week tweaks |

### 1. Strategist & Copywriter
- Pull next week's rows from the calendar; keep the weekly rhythm (Mon PF, Tue ESIC/Law, Wed Product, Thu Agency owner, Fri Tender/Compliance, Sat People).
- News scan (web search): epfindia.gov.in, esic.gov.in, labour.gov.in, the Gujarat labour department. A real, confirmed update gets an extra post within 24 hours; cite the circular in the LinkedIn caption.
- Captions: Instagram in Hinglish (short, emoji-light, 4–6 hashtags); LinkedIn in English (hook line, 3–5 value lines, CTA, 4–6 hashtags). CTA: free demo at zeniahr.com · Sales@zeniahr.com · +91 90998 87880.
- Apply the analyst's last recommendations (e.g. more carousels if saves are higher).

### 2. Creative Designer
- Follow the design kit exactly (grounds rotate navy → mist → copper by the running post index k).
- Hosting: images must have a public https URL for Zoho. Push to the public GitHub repo `PULPIT221090/zeniahr-social` under `assets/YYYY-MM-DD/` and use `https://raw.githubusercontent.com/PULPIT221090/zeniahr-social/main/assets/...`. If the repo isn't available, fall back to a Pexels image from Zoho's library (`getSocialMediaLibrary`, library_type "pexels") and report it.
- Check every render visually before handing over.

### 3. Publisher & Community
- Weekly: for each day, `createSocialSchedule` (type 1) at 10:47 IST, channels linkedinpage + instagram, one message with medias (carousel = several medias). Skip any day already scheduled (`listSocialSchedules`).
- Daily (07:41 IST): `listSocialSchedules is_failed=true`, then retry once or report. `getSocialPostActivities` on the last 7 days of posts: list new comments and draft replies for Yogesh. Do NOT post replies automatically.

### 4. Performance Analyst
- Data: `getSocialPublishedPosts` + `getSocialPublishedPostDetail` (reach, impressions, likes, comments, shares, saves, clicks) per channel.
- KPIs: engagement rate by reach, saves + shares per post, profile/website clicks, demo enquiries (ask Yogesh weekly), follower growth.
- Compare by template family, category, language (Hinglish vs English), format (static/carousel/motion) and posting time.
- Search: Google Search Console for zeniahr.com (queries, clicks, CTR, top pages) is NOT connected yet. Once a GSC connector is connected, add clicks/impressions for labour-law pages and link posts to landing pages.
- LinkedIn Ads / boosting: not connected. Recommend 1–2 winning organic posts per month to boost (₹ budget decided by Yogesh).

## Tested platform limits (Sep 2026)
- Image hosting works: public repo `PULPIT221090/zeniahr-social`, raw.githubusercontent.com URLs. Design kit + manifest (running index k) live in `kit/`. Last k used: 13 (15 Oct).
- MP4 video via the Zoho MCP fails ("try scheduling after some time"). Schedule motion posts with their `_cover.jpg`; list the MP4s in the report so Yogesh can post them as Reels in the Zoho app. A failed video attempt still leaves an empty schedule behind: after any failure, run listSocialSchedules and delete schedules that have no medias.
- LinkedIn native polls (`poll` key) are rejected with EXTRA_KEY_FOUND_IN_JSON; use the poll image + 'reply A/B/C/D'.
- Instagram and LinkedIn get SEPARATE schedules (Hinglish IG caption, English LinkedIn caption), same image(s), 10:47 IST. Carousel = several medias.
- 1–15 Oct 2026 is already scheduled (28 posts). The weekly run must continue from 16 Oct.

## What still needs Yogesh
1. (Done) Public GitHub repo.
2. Official ZeniaHR logo file (PNG/SVG) for the profile picture and end cards.
3. Google Search Console access (a connector, or a monthly CSV export) for zeniahr.com.
4. Weekly count of demo enquiries from social (from Zoho CRM/Bigin if tagged).
