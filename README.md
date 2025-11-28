<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Django E-Commerce REST API — README</title>
  <style>
    :root{--bg:#0f172a;--card:#0b1220;--muted:#94a3b8;--accent:#7c3aed;--glass:rgba(255,255,255,0.04)}
    body{font-family:Inter,ui-sans-serif,system-ui,Segoe UI,Roboto,Helvetica,Arial;line-height:1.6;margin:0;background:linear-gradient(180deg,#071024 0%, #071827 100%);color:#e6eef8}
    .wrap{max-width:980px;margin:36px auto;padding:28px;background:linear-gradient(180deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,0.6)}
    header{display:flex;align-items:center;gap:16px;margin-bottom:18px}
    .logo{width:56px;height:56px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#0ea5a4);display:flex;align-items:center;justify-content:center;font-weight:700;color:white}
    h1{margin:0;font-size:1.6rem}
    p.lead{margin:6px 0 18px;color:var(--muted)}
    nav.toc{background:var(--glass);padding:14px;border-radius:10px;margin-bottom:20px}
    nav.toc ul{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:8px}
    nav.toc a{color:#cfe7ff;text-decoration:none;padding:6px 10px;background:rgba(255,255,255,0.02);border-radius:8px;font-size:0.9rem}
    section{margin-bottom:18px;padding:16px;background:transparent;border-radius:8px}
    h2{margin:0 0 8px;color:#dbeafe}
    pre,code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:#021224;padding:10px;border-radius:8px;overflow:auto}
    table{width:100%;border-collapse:collapse;margin-top:8px}
    table th,table td{border:1px solid rgba(255,255,255,0.04);padding:8px;text-align:left}
    footer{font-size:0.85rem;color:var(--muted);margin-top:22px;border-top:1px dashed rgba(255,255,255,0.03);padding-top:12px}
    .small{color:var(--muted);font-size:0.95rem}
    .pill{display:inline-block;padding:6px 10px;border-radius:999px;background:rgba(255,255,255,0.03);font-size:0.85rem}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">API</div>
      <div>
        <h1>Django E-Commerce REST API — README</h1>
        <p class="lead">A production-minded README for a modular Django + DRF backend (JWT authentication, products, cart, orders, tests, and docs).</p>
      </div>
    </header>

    <nav class="toc" aria-label="Table of contents">
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#stack">Tech Stack</a></li>
        <li><a href="#structure">Project Structure</a></li>
        <li><a href="#install">Installation</a></li>
        <li><a href="#config">Configuration</a></li>
        <li><a href="#auth">Authentication</a></li>
        <li><a href="#endpoints">API Endpoints</a></li>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#errors">Common Errors</a></li>
        <li><a href="#roadmap">Roadmap</a></li>
      </ul>
    </nav>

    <section id="overview">
      <h2>Overview</h2>
      <p>This repository implements a RESTful backend for a small e‑commerce platform. The API supports:</p>
      <ul>
        <li>User creation and JWT login</li>
        <li>Product CRUD (create, read, update, delete)</li>
        <li>Cart management per authenticated user</li>
        <li>Order creation and listing for authenticated users</li>
        <li>Automated tests using <span class="pill">pytest</span></li>
        <li>API docs via Swagger (drf-yasg)</li>
      </ul>
    </section>

    <section id="features">
      <h2>Features</h2>
      <ul>
        <li>JWT auth with access + refresh tokens</li>
        <li>Role-ready endpoints (can add admin/seller roles)</li>
        <li>Strict per-user access control on cart & orders</li>
        <li>Well-structured tests for models & APIs</li>
      </ul>
    </section>

    <section id="stack">
      <h2>Tech Stack</h2>
      <table>
        <tr><th>Backend</th><td>Django 4.2, Django REST Framework</td></tr>
        <tr><th>Auth</th><td>Simple JWT (djangorestframework-simplejwt)</td></tr>
        <tr><th>Docs</th><td>drf-yasg (Swagger)</td></tr>
        <tr><th>Testing</th><td>pytest, pytest-django, factory_boy</td></tr>
        <tr><th>DB (default)</th><td>SQLite (development) — swapable for Postgres/MySQL</td></tr>
      </table>
    </section>

    <section id="structure">
      <h2>Project Structure</h2>
      <pre><code>Ecommerce/
├── users/       # custom user model, serializers, views, urls, tests
├── products/    # product model, serializers, viewsets, tests
├── cart/        # cart model, serializer, viewset, tests
├── orders/      # order model, serializer, viewset, tests
├── Ecommerce/   # project settings & urls
├── manage.py
├── pytest.ini
└── requirements.txt
</code></pre>
    </section>

    <section id="install">
      <h2>Installation</h2>
      <ol>
        <li>Clone the repo: <code>git clone &lt;repo&gt;</code></li>
        <li>Create virtualenv: <code>python -m venv venv &amp;&amp; source venv/bin/activate</code></li>
        <li>Install: <code>pip install -r requirements.txt</code></li>
        <li>Run migrations: <code>python manage.py migrate</code></li>
        <li>Create admin: <code>python manage.py createsuperuser</code></li>
        <li>Run server: <code>python manage.py runserver</code></li>
      </ol>
    </section>

    <section id="config">
      <h2>Configuration</h2>
      <p>Recommended environment variables (use <code>.env</code> with django-environ or os.environ):</p>
      <pre><code>DEBUG=True
SECRET_KEY=your-secret
DATABASE_URL=sqlite:///db.sqlite3
</code></pre>
      <p class="small">To use Postgres: set <code>DATABASE_URL=postgres://user:pass@host:port/db</code> and update requirements.</p>
    </section>

    <section id="auth">
      <h2>Authentication (JWT)</h2>
      <p>Token endpoints are available:</p>
      <ul>
        <li><code>POST /api/token/</code> — returns <code>access</code> &amp; <code>refresh</code></li>
        <li><code>POST /api/token/refresh/</code> — refresh access token</li>
      </ul>
      <p>Protected endpoints require header:</p>
      <pre><code>Authorization: Bearer &lt;access_token&gt;</code></pre>
    </section>

    <section id="endpoints">
      <h2>API Endpoints</h2>

      <h3>Users</h3>
      <table>
        <tr><th>Method</th><th>URL</th><th>Notes</th></tr>
        <tr><td>POST</td><td>/api/users/register/</td><td>Register new user (email, username, password)</td></tr>
        <tr><td>POST</td><td>/api/token/</td><td>Login (get tokens)</td></tr>
      </table>

      <h3>Products</h3>
      <table>
        <tr><th>Method</th><th>URL</th><th>Notes</th></tr>
        <tr><td>GET</td><td>/api/products/</td><td>List</td></tr>
        <tr><td>POST</td><td>/api/products/</td><td>Create (auth required)</td></tr>
        <tr><td>GET/PATCH/DELETE</td><td>/api/products/{id}/</td><td>Retrieve/update/delete</td></tr>
      </table>

      <h3>Cart</h3>
      <p>Cart is per authenticated user.</p>
      <table>
        <tr><th>Method</th><th>URL</th><th>Notes</th></tr>
        <tr><td>GET</td><td>/api/cart/</td><td>List current user cart items</td></tr>
        <tr><td>POST</td><td>/api/cart/</td><td>Add item (product, quantity)</td></tr>
        <tr><td>PATCH/DELETE</td><td>/api/cart/{id}/</td><td>Update/remove item</td></tr>
      </table>

      <h3>Orders</h3>
      <table>
        <tr><th>Method</th><th>URL</th><th>Notes</th></tr>
        <tr><td>GET</td><td>/api/orders/</td><td>List orders (current user)</td></tr>
        <tr><td>POST</td><td>/api/orders/</td><td>Create order (product, quantity)</td></tr>
      </table>
    </section>

    <section id="testing">
      <h2>Testing</h2>
      <p>The project uses <code>pytest</code> and <code>pytest-django</code>. Example commands:</p>
      <pre><code>pip install -r requirements-dev.txt
pytest -q
pytest path/to/test_file.py::test_specific_case
</code></pre>
      <p>Make sure any custom fixtures are defined in <code>tests/conftest.py</code>. Example fixtures used by this project:</p>
      <pre><code># tests/conftest.py (example)
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_client(db):
    client = APIClient()
    user = User.objects.create_user(email='user@example.com', username='user', password='test123')
    client.force_authenticate(user=user)
    return client
</code></pre>
    </section>

    <section id="errors">
      <h2>Common Errors &amp; Fixes</h2>
      <dl>
        <dt><strong>405 Method Not Allowed on /api/cart/</strong></dt>
        <dd>Make sure your router registration matches expected path. If router registers <code>cart/</code> as prefix, your client should POST to <code>/api/cart/cart/</code> — register router with an empty prefix or adjust tests/requests to correct URL. Example router registration for top-level <code>/api/cart/</code> endpoints:
          <pre><code># cart/urls.py
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register('', CartViewSet, basename='cart')

urlpatterns = [
  path('', include(router.urls)),
]
</code></pre>
        </dd>

        <dt><strong>400 Bad Request when creating objects</strong></dt>
        <dd>Inspect serializer errors returned in response; required fields may be missing (e.g. seller field for Product). For viewsets that auto-fill fields use <code>perform_create</code>:
          <pre><code>def perform_create(self, serializer):
    serializer.save(seller=self.request.user)
</code></pre>
        </dd>

        <dt><strong>Fixtures missing in pytest</strong></dt>
        <dd>Ensure <code>tests/conftest.py</code> defines fixtures like <code>api_client</code> and <code>auth_client</code>. Run <code>pytest --fixtures</code> to list available fixtures.</dd>
      </dl>
    </section>

    <section id="roadmap">
      <h2>Roadmap</h2>
      <ul>
        <li>Payment integration (Stripe/PayPal)</li>
        <li>Product categories &amp; tagging</li>
        <li>Search &amp; advanced filtering</li>
        <li>Background tasks for order processing (Celery)</li>
        <li>Admin analytics &amp; dashboards</li>
      </ul>
    </section>

    <footer>
      <div>Author: <strong>Ninad Badekar</strong> • Backend: Django + DRF • License: MIT</div>
      <div class="small">Generated README HTML — copy this file to your project root as <code>README.html</code> or open in a browser.</div>
    </footer>
  </div>
</body>
</html>
