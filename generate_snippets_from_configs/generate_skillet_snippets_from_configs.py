# 12-12-19 nembery@paloaltonetworks.com
from skilletlib import Panoply
import os
import sys
import json

# grab our two configs from the environment
base_config = os.environ.get('BASE_CONFIG', '')
latest_config = os.environ.get('LATEST_CONFIG', '')

# init the Panoply helper class, note we do not need connection information, as we only need offline mode
# to compare two configurations
p = Panoply()

# insert magic here
snippets = p.generate_skillet_from_configs(base_config, latest_config)

# check we actually have some diffs
if len(snippets) == 0:
    print('No Candidate Configuration can be found to use to build a skillet!')
    sys.exit(2)

# dump out our diffs here. Note, we will use output capturing in the skillet to capture this
print(json.dumps(snippets, indent=2))

# later gator
sys.exit(0)