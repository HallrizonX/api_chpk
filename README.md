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
        <li><b>/profiles/:id/</b> [GET Authorization: JWT <token>] Get detail profile.<hr></li>
        <li><b>/teachers/files/</b> [GET Authorization: JWT <token>] Get all files for current teacher filter by token</li>
        <li><b>/teachers/</b> [GET Authorization: JWT <token>] Get list of teachers.</li>
        <li><b>/teachers/:id/</b> [GET Authorization: JWT <token>] Get detail teacher by id.<hr></li>
        <li><b>/groups/teachers/:group number</b> [GET Authorization: JWT <token>] Get list of teachers filtered by group number.</li>
        <li><b>/groups/subjects/:group number</b> [GET Authorization: JWT <token>] Get list of subjects filtered by group number.</li>
        <li><b>/groups/</b> [GET Authorization: JWT <token>] Get list of groups.</li>
        <li><b>/groups/:id/</b> [GET Authorization: JWT <token>] Get detail group by id.<hr></li>
        <li><b>/subjects/</b> [GET Authorization: JWT <token>] Get list of subjects.</li>
        <li><b>/subjects/:id/</b> [GET Authorization: JWT <token>] Get deteail subject.</li>
        <li><b>/subjects/teachers/:subject id/</b> [GET Authorization: JWT <token>] Get current teacher for deatail subject<hr></li>
        <li><b>/news/</b> [GET Authorization: JWT <token>] Get list of news</li>
        <li><b>/news/:id/</b> [GET Authorization: JWT <token>] Get current news by ID</li>
    </ul>
</ul>