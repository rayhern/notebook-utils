from requests import Session
import traceback
import requests

def download_file(file_url: str, savefile_path: str, encoding: str = "utf8", timeout: int = 200, session: Session = None):
    try:
        if session is None:
          session = Session()
        r = session.get(
            file_url, headers=headers, allow_redirects=True, timeout=timeout)
        open(savefile_path, 'wb').write(r.content)
    except:
        print(traceback.format_exc())
