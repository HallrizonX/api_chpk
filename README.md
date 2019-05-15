<h1>Main Versions</h1>
<p>Python version: 3.7.1</p>
<p>Django version: 2.0.6</p>
<p>Django REST Framework version: 3.7.7</p>
<p>DataBase SQLlite</p>
<hr>
<h1>All routers</h1>
<ul>JSON Web Token
    <ul>
        <li><b>/auth/jwt/create/</b> [POST {username, password}] Create JWT.</li>
        <li><b>/auth/jwt/refresh/</b> [POST {token:EXIST Token}, application/json] Refresh JWT.</li>
        <li><b>/auth/jwt/verify/</b> [POST {token:EXIST Token}, application/json] Verify JWT.</li>
    </ul>
</ul>
<ul>API
    <ul>
        <li><b>/profiles/</b> [GET Authorization: JWT <token>] All profiles.</li>
        <li><b>/profiles/:id/</b> [GET Authorization: JWT <token>] Get detail profile.</li>
    </ul>
</ul>