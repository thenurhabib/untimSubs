#!/usr/bin python3

__Version__ = "v1.0.0"

reset='\033[0m'
bold='\033[01m'
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'



def bannerFunc():
    print(f"""{bold}{yellow}
               __  _          _____       __        
  __  ______  / /_(_)___ ___ / ___/__  __/ /_  _____
 / / / / __ \/ __/ / __ `__ \\\__ \/ / / / __ \/ ___/
/ /_/ / / / / /_/ / / / / / /__/ / /_/ / /_/ (__  ) 
\__,_/_/ /_/\__/_/_/ /_/ /_/____/\__,_/_.___/____/{red}  {__Version__}
{blue}
It makes easy to use all subdomain enumeration with all popular tools.

{purple} develop by {cyan} @thenurhabib {reset}
    """)