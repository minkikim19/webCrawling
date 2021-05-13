print(
    "page url:{}, http status: {}, processing time(sec): {}".format(
        page_url,
        res.status_code,
        res.elapsed.total_seconds()
    )
)