# FitBite — SEO & Email Marketing Lead Generation Campaign

A complete beginner-friendly portfolio project for demonstrating SEO, email marketing, lead generation, landing-page optimization, content marketing, analytics and conversion optimization.

> **Data integrity:** FitBite is fictional. Dashboard/email figures are explicitly simulated. The project does not claim real customers, conversions, rankings, social engagement, email results or a live Google Business Profile.

## 1. What this project demonstrates

- Responsive HTML5 + Bootstrap 5 website
- Django backend and admin
- MySQL database support
- Lead form with validation and marketing consent
- Duplicate-email protection
- Lead statuses: New, Contacted, Interested, Converted, Unsubscribed
- Newsletter signup
- UTM capture
- Five-email campaign plan
- Four audience segments
- Five SEO blog topics
- SEO titles/meta descriptions/canonical URLs
- Django sitemap and robots.txt
- 404 page
- Demo marketing dashboard
- Chart.js source chart
- Campaign report / case study
- Interview preparation notes with English + Tanglish + project example
- Resume bullets
- Render deployment configuration
- SMTP environment variables

## 2. Project structure

```text
fitbite/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── render.yaml
├── build.sh
├── config/
├── marketing/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── sitemaps.py
│   ├── management/commands/seed_demo.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── 404.html
│   ├── marketing/
│   └── emails/
├── static/
│   ├── css/style.css
│   ├── js/app.js
│   └── images/favicon.svg
└── docs/
    ├── keyword-research.xlsx
    ├── content-calendar.xlsx
    ├── email-campaigns.md
    ├── seo-checklist.md
    ├── local-seo-strategy.md
    ├── social-media-strategy.md
    ├── campaign-report.md
    ├── interview-prep.md
    ├── resume-output.md
    └── stack-explained.md
```

## 3. Windows + VS Code setup

### Install
1. Install Python 3.12+.
2. Install MySQL 8.
3. Install Git.
4. Install VS Code.
5. Open this project folder in VS Code.

### Create virtual environment

PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Create MySQL database

In MySQL:

```sql
CREATE DATABASE fitbite CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'fitbite_user'@'localhost' IDENTIFIED BY 'fitbite_password';
GRANT ALL PRIVILEGES ON fitbite.* TO 'fitbite_user'@'localhost';
FLUSH PRIVILEGES;
```

Copy `.env.example` to `.env` and adjust credentials.

For local MySQL, use the `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, and `MYSQL_PORT` variables. Render uses `DATABASE_URL` instead.

### Migrate + seed

```powershell
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Home: http://127.0.0.1:8000/
- Campaign: http://127.0.0.1:8000/campaign/
- Blog: http://127.0.0.1:8000/blog/
- Dashboard: http://127.0.0.1:8000/dashboard/
- Admin: http://127.0.0.1:8000/admin/
- Sitemap: http://127.0.0.1:8000/sitemap.xml
- Robots: http://127.0.0.1:8000/robots.txt

## 4. Test the lead funnel

1. Open `/campaign/`.
2. Submit a valid lead.
3. Confirm the success message.
4. Open `/admin/` → Leads.
5. Confirm the lead was stored.
6. Submit the same email again to see duplicate protection.
7. Check that the subscriber was created.
8. Open `/dashboard/`.

## 5. Email setup

The project is SMTP-ready. Put credentials in `.env` only.

Required variables:

```text
EMAIL_HOST=
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=
```

Never commit `.env`.

The project also contains HTML templates for five email types. Brevo or Mailchimp can be connected later for actual campaign automation.

## 6. GA4 + Search Console

Set:

```text
GA4_MEASUREMENT_ID=G-XXXXXXXXXX
GSC_VERIFICATION=your-verification-token
```

If these are blank, the site remains usable without those external services.

## 7. Render deployment — fastest path

Render's current Django deployment guidance uses a build script, Gunicorn and environment variables. This repository already contains `build.sh` and `render.yaml` for the web service.

### A. Push to GitHub

```powershell
git init
git add .
git commit -m "Build FitBite marketing portfolio project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/fitbite.git
git push -u origin main
```

### B. Create MySQL on Render

Render documents MySQL as a private service backed by a persistent disk. Create a MySQL 8 service in the same Render workspace as the web service.

Use the internal MySQL connection details to create your Django `DATABASE_URL`, for example:

```text
mysql://USERNAME:PASSWORD@MYSQL_INTERNAL_HOST:3306/DATABASE_NAME
```

Do not copy this example literally; use the actual credentials generated for your service.

### C. Deploy the web service

1. In Render, create a **New Blueprint** from the GitHub repository, or create a Python Web Service manually.
2. Use `./build.sh` as the build command.
3. Use `python -m gunicorn config.wsgi:application` as the start command.
4. Add the environment variables listed in `.env.example`.
5. Set `DATABASE_URL` to your Render MySQL connection string.
6. Set `DEBUG=False`.
7. Set `ALLOWED_HOSTS` to your Render hostname.
8. Set `SITE_URL` to your HTTPS Render URL.
9. Deploy.
10. Open the Render Shell and run `python manage.py createsuperuser`.
11. Visit `/admin/` to verify the database connection.

### Important Render note

Render's managed Django quick-start examples use PostgreSQL, but Render also documents deploying MySQL as a private service. This project deliberately remains MySQL-first to match the portfolio brief. See the deployment links below.

## 8. Deployment verification checklist

- [ ] Homepage loads with HTTPS
- [ ] `/campaign/` loads
- [ ] Lead form submits
- [ ] Duplicate email is blocked
- [ ] `/admin/` works
- [ ] `/dashboard/` shows demo metrics
- [ ] `/sitemap.xml` returns XML
- [ ] `/robots.txt` returns text
- [ ] 404 page works
- [ ] Static CSS/JS loads
- [ ] No secrets are committed
- [ ] Demo data is labeled simulated

## 9. Portfolio walkthrough

When presenting the project, explain it in this order:

1. Business problem and target audience
2. Keyword intent → page mapping
3. SEO implementation
4. Campaign landing page and CTA
5. Lead form and consent
6. Email segmentation and five-email funnel
7. A/B testing
8. Analytics dashboard
9. 30-day campaign plan
10. What you would do next with real data

## 10. Interview safety rule

Say “I designed / implemented / simulated” for this portfolio project. Do not say “I generated 500 real leads” or “I ranked #1” unless you have real evidence.


## QA before deployment

Use `docs/manual-testing-checklist.md` and complete the full manual test pass before pushing to Render.
