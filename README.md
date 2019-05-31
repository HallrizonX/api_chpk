<h1>Main Versions</h1>
<p>Python version: <b>3.7.1</b></p>
<p>Django version: <b>2.0.6</b></p>
<p>Django REST Framework version: <b>3.7.7</b></p>
<p>DataBase: SQLlite(dev)</p>
<p>Cache: Redis Server</p>
<hr>
<h1>All routers</h1>
<ul>JSON Web Token
    <ul>
        <li><b>/auth/jwt/create/</b> [POST {username, password}] Create JWT.</li>
        <li><b>/auth/jwt/refresh/</b> [POST {token:EXIST Token}, application/json] Refresh JWT.</li>
        <li><b>/auth/jwt/verify/</b> [POST {token:EXIST Token}, application/json] Verify JWT.</li>
    </ul>
</ul>
<ul>API (adding '/api/v1/' for every links)
    <ul>
        <li> <h4>Work with profiles</h4></li>
        <li><b>/profiles/</b> [GET Authorization: JWT <token>] All profiles.</li>
        <li><b>/profiles/:id/</b> [GET Authorization: JWT <token>] Get detail profile.<hr></li>
        <li> <h4>Work with teachers</h4></li>
        <li><b>/teachers/files/</b> [GET Authorization: JWT <token>] <b>Security</b> get all files for current teacher who was did authorizations by token</li>
        <li><b>/teachers/files/:file_id/</b> [GET Authorization: JWT <token>] <b>Security</b> get file chose by id and for current teacher who was did authorizations by token</li>
        <li><b>/teachers/</b> [GET Authorization: JWT <token>] Get list of teachers.</li>
        <li><b>/teachers/:id/</b> [GET Authorization: JWT <token>] Get detail teacher by id</li>
        <li><b>/teachers/:id/files/</b> [GET/POST Authorization: JWT <token>] Get all files for teacher filtered by id.</li>
        <li><b>/teachers/:id/files/:file_id/</b> [GET/PUT/PUTCH/DELETE Authorization: JWT <token>] Working with file such as remove file, update data to file<hr></li>
        <li> <h4>Work with groups</h4></li>
        <li><b>/groups/:group_number/teachers/</b> [GET Authorization: JWT <token>] Get list of teachers filtered by group number.</li>
        <li><b>/groups/:group number/subjects/</b> [GET Authorization: JWT <token>] Get list of subjects filtered by group number.</li>
        <li><b>/groups/</b> [GET Authorization: JWT <token>] Get list of groups.</li>
        <li><b>/groups/:id/</b> [GET Authorization: JWT <token>] Get detail group by id.</li>
        <li><b>/groups/:id/teachers/</b> [GET Authorization: JWT <token>] Get list of teachers filtered by id.</li>
        <li><b>/groups/:id/subjects/</b> [GET Authorization: JWT <token>] Get list of subjects filtered by id.<hr></li>
        <li> <h4>Work with subjects</h4></li>
        <li><b>/subjects/</b> [GET Authorization: JWT <token>] Get list of subjects.</li>
        <li><b>/subjects/:id/</b> [GET Authorization: JWT <token>] Get deteail subject.</li>
        <li><b>/subjects/:id/teachers/</b> [GET Authorization: JWT <token>] Get all teachers for deatail subject</li>
        <li><b>/subjects/:id/files/</b> [GET Authorization: JWT <token>] Get all files for deatail subject<hr></li>
        <li> <h4>Work with articles</h4></li>
        <li><b>/news/</b> [GET Authorization: JWT <token>] Get list of news</li>
        <li><b>/news/:id/</b> [GET Authorization: JWT <token>] Get current news by ID<hr></li>
        <li> <h4>Work with journal</h4></li>
        <li><b>/teacher/journals/</b> [GET Authorization: JWT <token>] Get list of journals for current teacher where he explaining</li>
        <li><b>/student/journals/</b> [GET Authorization: JWT <token>] Get list of journals for current student where he study</li>
        <li><b>/journals/:group_number/groups/</b> [GET Authorization: JWT <token>] Get list of journals filtered by group</li>
        <li><b>/journals/:id/</b> [GET Authorization: JWT <token>] Get current journal</li>
        <li><b>/journals/</b> [GET Authorization: JWT <token>] Get list of all journals</li>
        <li><b>/marks/</b> [GET Authorization: JWT <token>] Get list of all marks</li>
        <li><b>/marks/:id/</b> [GET/PUT/PUTCH/DELETE Authorization: JWT <token>] Wokring with marks</li>
    </ul>
</ul>