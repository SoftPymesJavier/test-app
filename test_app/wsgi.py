# -*- coding: utf-8 -*-
#########################################################
import os
from app import app

if __name__ == "__main__":
    app.run(host=os.environ['HOST'],
            port=os.environ['PORT'],
            debug=True if int(os.environ['DEBUG']) else False)
