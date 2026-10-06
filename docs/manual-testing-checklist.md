# FitBite Manual Testing Checklist

Use this checklist before GitHub/Render deployment. Record PASS/FAIL and any notes.

## 1. Server and database

- [ ] `python manage.py check` passes.
- [ ] `python manage.py migrate` completes successfully.
- [ ] `python manage.py seed_demo` completes successfully.
- [ ] `python manage.py createsuperuser` creates a staff account.
- [ ] `python manage.py runserver` starts without an exception.

## 2. Public pages

- [ ] `/` loads.
- [ ] `/about/` loads.
- [ ] `/services/` loads.
- [ ] `/blog/` loads and shows seeded articles.
- [ ] Each blog detail URL loads.
- [ ] `/contact/` loads.
- [ ] `/campaign/` loads.
- [ ] `/campaign-report/` loads.
- [ ] `/robots.txt` returns plain text.
- [ ] `/sitemap.xml` returns valid XML.
- [ ] `/404-demo/` loads the designed 404 page.

## 3. Navigation and responsive UI

- [ ] Logo links to home.
- [ ] About, Meals, Healthy Living and Contact links work.
- [ ] Header CTA opens the campaign page.
- [ ] Mobile navigation opens/closes.
- [ ] Forms remain usable at mobile width.
- [ ] Buttons have visible hover/focus states.
- [ ] No horizontal scrolling at mobile width.

## 4. Lead generation

### Campaign form

- [ ] Valid submission succeeds.
- [ ] Successful submission redirects to `/thank-you/`.
- [ ] Thank-you page displays the success state.
- [ ] Lead appears in Django Admin.
- [ ] Subscriber appears in Django Admin.
- [ ] UTM parameters are stored when supplied.

### Validation

- [ ] Blank required name is rejected.
- [ ] Invalid email is rejected.
- [ ] Missing consent is rejected.
- [ ] Duplicate email is rejected cleanly.
- [ ] Optional phone can be blank.

### Contact form

- [ ] Valid contact submission also reaches `/thank-you/`.
- [ ] Invalid contact submission stays on the contact page and shows errors.

## 5. Newsletter

- [ ] Valid email creates a subscriber.
- [ ] Existing subscribed email does not create a duplicate.
- [ ] Existing unsubscribed email can be re-subscribed through a new consented lead.
- [ ] Invalid email is rejected.

## 6. Admin

- [ ] `/admin/` requires authentication.
- [ ] Leads can be searched.
- [ ] Lead status can be edited.
- [ ] Subscribers can be filtered.
- [ ] Blog posts can be edited.
- [ ] Email campaigns show simulated metrics.
- [ ] Campaign metrics show simulated data.

## 7. Marketing dashboard

- [ ] `/dashboard/` requires staff login.
- [ ] Chart renders after Chart.js loads.
- [ ] Funnel values render.
- [ ] Email campaign table renders.
- [ ] Recent leads render only for authenticated staff.
- [ ] DEMO / SIMULATED labels remain visible.

## 8. SEO

For each important page inspect page source:

- [ ] One clear H1.
- [ ] SEO title exists.
- [ ] Meta description exists.
- [ ] Canonical URL exists.
- [ ] Internal links work.
- [ ] No broken navigation URLs.

Technical:

- [ ] `/robots.txt` points to the sitemap.
- [ ] `/sitemap.xml` contains public pages and published blog URLs.
- [ ] Dashboard/admin are not intended for search indexing.
- [ ] Production `SITE_URL` is configured before deployment.

## 9. Demo-data integrity

- [ ] Dashboard and campaign metrics are labeled DEMO / SIMULATED.
- [ ] No fake rankings are claimed.
- [ ] No fake customer results are claimed.
- [ ] No fake email results are presented as real.
- [ ] No real Google Business Profile is claimed.
- [ ] Illustrative meal prices are labeled as portfolio/demo prices.

## 10. Deployment readiness

- [ ] `.env` is ignored by Git.
- [ ] No password/API key is committed.
- [ ] `requirements.txt` is complete.
- [ ] `build.sh` is executable/usable by Render.
- [ ] Render `DATABASE_URL` is configured separately from local `MYSQL_*` settings.
- [ ] `DEBUG=False` in production.
- [ ] `SITE_URL` uses HTTPS in production.
- [ ] `ALLOWED_HOSTS` contains the Render hostname.
- [ ] Static files collect successfully.

## 11. Browser console check

- [ ] Open browser DevTools → Console.
- [ ] Public pages have no application JavaScript errors.
- [ ] Dashboard has no Chart.js/JSON parsing error.
- [ ] Form submission has no JavaScript exception.

## 12. Database verification after form tests

In Django Admin confirm:

- [ ] Lead record contains the submitted name/email/city/meal preference.
- [ ] Lead status starts at `New`.
- [ ] Subscriber exists with `New subscriber` segment.
- [ ] Duplicate submission does not create a second lead.
