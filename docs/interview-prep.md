# FitBite Interview Preparation

Use these answers as speaking notes, not as a script.

## A. Explain your project.
**Simple English:** I built a fictional local healthy-food lead-generation campaign that connects SEO, a landing page, lead capture, email nurturing and analytics in one Django website.
**Tanglish:** “Naan oru local healthy-food business-ku SEO, landing page, lead generation, email funnel and analytics connect pannina portfolio project build panninen.”
**Project example:** FitBite uses keyword-focused pages, a campaign landing page and a five-step email sequence.

## B. What was your role?
**Simple English:** I handled the digital marketing strategy and built the supporting website features needed to demonstrate the funnel.
**Tanglish:** “Marketing strategy-um website implementation-um naan handle panninen; especially SEO, lead form, email flow and dashboard.”
**Project example:** I mapped keywords to pages and created the lead and campaign models in Django.

## C. How did you perform keyword research?
**Simple English:** I grouped keywords by search intent and mapped them to the most relevant page. I did not invent search volume.
**Tanglish:** “Keyword volume guess pannaama, intent based-a primary, secondary, long-tail keywords group panninen.”
**Project example:** “healthy food delivery” is mapped to core service content; “healthy lunch delivery” supports lunch-focused content.

## D. What is on-page SEO?
**Simple English:** On-page SEO is optimizing content and HTML elements on a page so the topic and intent are clear.
**Tanglish:** “Page-kulla title, meta, headings, content, keywords, internal links optimize pannradhu on-page SEO.”
**Project example:** FitBite pages have titles, descriptions, H1s and internal links.

## E. What is technical SEO?
**Simple English:** Technical SEO improves crawlability, indexability, site structure and performance.
**Tanglish:** “Search engine site-a crawl and index panna easy-a technical setup correct-a irukkanum.”
**Project example:** Sitemap, robots.txt, canonical tags, clean URLs and responsive design.

## F. What is off-page SEO?
**Simple English:** Off-page SEO refers to external signals such as legitimate links, mentions and reviews.
**Tanglish:** “Website-ku veliya irukkura trust signals like genuine backlinks, mentions, reviews off-page SEO-la varum.”
**Project example:** The local SEO document proposes genuine citations and reviews but does not claim any exist.

## G. What is a meta description?
**Simple English:** It is a short page summary that can help searchers understand the result before clicking.
**Tanglish:** “Search result-la page enna pathi-nu short summary kudukkura text.”
**Project example:** Each key page has a custom meta description.

## H. What is a sitemap?
**Simple English:** A sitemap lists important URLs so search engines can discover them more easily.
**Tanglish:** “Important URLs list-a search engine discover panna help pannradhu sitemap.”
**Project example:** Django generates `/sitemap.xml`.

## I. What is robots.txt?
**Simple English:** It gives crawlers instructions about which areas they may or may not crawl.
**Tanglish:** “Crawler-ku basic access instructions kudukkura file.”
**Project example:** FitBite exposes a robots endpoint that references the sitemap.

## J. What is email segmentation?
**Simple English:** Segmentation groups subscribers based on useful characteristics or behavior so messages are more relevant.
**Tanglish:** “Ella users-kum same mail anuppaama, behavior or stage based-a group pannradhu segmentation.”
**Project example:** New subscribers receive welcome content; interested users receive the offer sequence.

## K. What is email automation?
**Simple English:** Automation sends a planned message based on a trigger, event or schedule.
**Tanglish:** “User action or time trigger aagumbodhu planned email automatically send aagardhu.”
**Project example:** A new subscriber can enter the welcome → education → promotion sequence.

## L. What is open rate?
**Simple English:** Open rate is the percentage of delivered emails recorded as opened.
**Tanglish:** “Delivered emails-la evlo percentage open pannanga-nu measure pannradhu.”
**Project example:** Dashboard calculates it from opened divided by delivered.

## M. What is click-through rate?
**Simple English:** CTR measures the percentage of delivered emails that generated a click, using the campaign’s chosen denominator.
**Tanglish:** “Email-la click varra rate; denominator clearly define pannanum.”
**Project example:** This demo uses clicked divided by delivered.

## N. What is conversion rate?
**Simple English:** Conversion rate is the percentage of relevant visitors or recipients who complete the target action.
**Tanglish:** “Target action complete pannina users percentage.”
**Project example:** The campaign can measure landing-page lead conversion or email-to-conversion separately.

## O. What is bounce rate?
**Simple English:** For email, a bounce is an undelivered message; for web analytics, bounce rate is a different metric. Always clarify the context.
**Tanglish:** “Email bounce and website bounce rate same concept illa; context clear-a sollanum.”
**Project example:** EmailCampaign has bounced_count for delivery failures.

## P. What is A/B testing?
**Simple English:** A/B testing compares two controlled variants to learn which performs better against a predefined metric.
**Tanglish:** “Two versions compare panni, predefined KPI base-la winner decide pannradhu A/B testing.”
**Project example:** Two promotional subject lines are compared using conversion rate as the primary decision metric.

## Q. How do you improve email open rate?
**Simple English:** Improve audience relevance, subject lines, preview text, timing and list quality, then test systematically.
**Tanglish:** “Right audience, better subject, preview text, timing and clean list use panni test pannuvom.”
**Project example:** Test the two promotional subject lines.

## R. How do you improve email CTR?
**Simple English:** Make the CTA clear, align it with the email promise, reduce competing links and improve landing-page continuity.
**Tanglish:** “One clear CTA, email promise-kku match aagura landing page, less distraction.”
**Project example:** Promotional email CTA points directly to the campaign landing page.

## S. How do you generate leads?
**Simple English:** Match intent with a useful offer, remove unnecessary form friction, provide clear consent language and measure the source.
**Tanglish:** “Intent match aagura offer, simple form, consent and UTM tracking use panni lead generate pannuvom.”
**Project example:** FitBite captures name, email, meal preference, city and consent.

## T. How do you measure campaign success?
**Simple English:** Start with the business goal, define primary and secondary KPIs, compare performance by source and test improvements.
**Tanglish:** “Goal first define panni, KPI set panni, source and funnel stage compare panni optimize pannuvom.”
**Project example:** Lead conversion is primary; traffic, CTA clicks, email CTR and conversions are supporting measures.
