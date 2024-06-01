import json
import os

# Read the JSON data
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'info.json')

with open(filename, 'r', encoding='utf-8') as json_file:
    movies = json.load(json_file)

# HTML template for movie detail page
html_template = """
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="movieDetailStyles.css">
    <style>
        .movie-details-bg {{
            background-image: url('{poster}');
        }}
    </style>
</head>

<body>
    <header>
        <a href="index.html">
            <div class="logo">FilmChoice</div>
        </a>
        <nav>
            <ul>
                <li><a href="search.html">검색</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="movie-details">
            <div class="movie-details-bg"></div>
            <div class="movie-details-content">
                <div class="movie-details-text">
                    <h1 class="movie-title">{title}</h1>
                    <div class="movie-info">
                        <dl>
                            <dt>개봉</dt>
                            <dd>{release}</dd>
                            <dt>등급</dt>
                            <dd>{rating}</dd>
                            <dt>장르</dt>
                            <dd>{genre}</dd>
                            <dt>국가</dt>
                            <dd>{country}</dd>
                            <dt>러닝타임</dt>
                            <dd>{runtime}분</dd>
                            <dt>배급</dt>
                            <dd>{distributor}</dd>
                        </dl>
                    </div>
                    <button type="button" id="book-button">예매하기</button>
                    <div id="dropdown-menu" class="dropdown-menu">
                        <button class="cgv-button" onclick="window.location.href='{cgv_link}'">
                            <img height="24" src="cgv.svg" />
                        </button>
                        <button class="lottecinema-button"
                            onclick="window.location.href='{lottecinema_link}'">
                            <img height="24" src="lottecinema.svg" />
                        </button>
                        <button class="megabox-button"
                            onclick="window.location.href='{megabox_link}'">
                            <img height="24" src="megabox.svg" />
                        </button>
                        <button class="cineq-button"
                            onclick="window.location.href='{cineq_link}'">
                            <img height="24" src="cineq.svg" />
                        </button>
                    </div>
                </div>
                <img src="{poster}" class="highlight-img" alt="{title}">
            </div>
        </section>
        <h2>소개</h2>
        <p class="introduction">{introduction}</p>
        <h2>감독</h2>
        <p>{director}</p>
        <h2>출연</h2>
        <p>{cast}</p>
        <h2>누적 관객수</h2>
        <p>{audience}만명</p>
        <h2>평점</h2>
        <p>{score}</p>
    </main>
    <footer>
        <div class="inner">
            <div class="footer-message">이 페이지는 교육적 목적으로 제작되었습니다.</div>
            <div class="footer-contact">정준서 / joonseo1227@gachon.ac.kr</div>
        </div>
    </footer>
    <script>
        document.getElementById('book-button').addEventListener('click', function () {{
            var menu = document.getElementById('dropdown-menu');
            if (menu.classList.contains('show')) {{
                menu.classList.remove('show');
            }} else {{
                menu.classList.add('show');
            }}
        }});

        window.onclick = function (event) {{
            if (!event.target.matches('#book-button')) {{
                var dropdowns = document.getElementsByClassName('dropdown-menu');
                for (var i = 0; i < dropdowns.length; i++) {{
                    var openDropdown = dropdowns[i];
                    if (openDropdown.classList.contains('show')) {{
                        openDropdown.classList.remove('show');
                    }}
                }}
            }}
        }};
    </script>
</body>

</html>
"""

# Create output directory for HTML files
output_dir = 'moviePages'
os.makedirs(output_dir, exist_ok=True)

# Generate an HTML file for each movie
for movie in movies:
    title = movie["제목"]
    release = movie["개봉"]
    rating = movie["등급"]
    genre = movie["장르"]
    country = movie["국가"]
    runtime = movie["러닝타임"]
    distributor = movie["배급"]
    introduction = movie["소개"]
    director = movie["감독"]
    cast = movie["출연"]
    audience = movie["누적 관객수"]
    score = movie["평점"]
    poster = movie["포스터"]
    cgv_link = movie["CGV"]
    lottecinema_link = movie["롯데시네마"]
    megabox_link = movie["메가박스"]
    cineq_link = movie["씨네큐"]

    # Fill the HTML template with movie data
    html_content = html_template.format(
        title=title,
        release=release,
        rating=rating,
        genre=genre,
        country=country,
        runtime=runtime,
        distributor=distributor,
        introduction=introduction,
        director=director,
        cast=cast,
        audience=audience,
        score=score,
        poster=poster,
        cgv_link=cgv_link,
        lottecinema_link=lottecinema_link,
        megabox_link=megabox_link,
        cineq_link=cineq_link
    )

    filename = poster.split('.')[0]

    # Write the HTML content to a file
    html_filename = os.path.join(output_dir, f"{filename}.html")
    with open(html_filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

print(f"Generated {len(movies)} movie detail pages in the '{output_dir}' directory.")
