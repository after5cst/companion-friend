import logging
import uvicorn

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%M:%S",
)  # datefmt='%Y-%m-%d %H:%M:%S'


if __name__ == "__main__":
    logging.getLogger().addHandler(logging.StreamHandler())
    uvicorn.run(
        "comfriend.restful:app",
        host="127.0.0.1",
        port=5000,
        log_level="debug",
        reload=True,
    )
