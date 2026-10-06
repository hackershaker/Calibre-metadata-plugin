# __init__.py
# 여러 도서 API를 하나의 Calibre Metadata Source Plugin으로 통합하기 위한 기본 구조

from calibre.ebooks.metadata.sources.base import Source


class BookMetadata(Source):
    """도서 API를 이용해 Calibre에 도서 metadata를 제공한다."""

    name = "Book Metadata"
    description = "Metadata source for books"
    version = (0, 1, 0)
    author = "deltahackall"

    # 이 플러그인이 제공할 metadata 기능을 정의한다.
    capabilities = frozenset(("identify", "cover"))

    # 검색 결과로 가져올 metadata 필드를 정의한다.
    touched_fields = frozenset(
        (
            "title",
            "authors",
            "publisher",
            "pubdate",
            "identifiers",
            "tags",
            "comments",
            "cover",
        )
    )

    def identify(
        self,
        log,
        result_queue,
        abort,
        title=None,
        authors=None,
        identifiers={},
        timeout=30,
    ):
        # ISBN이 있으면 ISBN을 우선적으로 사용한다.
        isbn = identifiers.get('isbn')

        if isbn:
            log.info(f'ISBN 검색: {isbn}')
        elif title:
            log.info(f'제목 검색: {title}')
        else:
            log.info('검색할 ISBN 또는 제목이 없습니다.')
            return