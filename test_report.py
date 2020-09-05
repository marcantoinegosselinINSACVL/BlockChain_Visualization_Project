#########################################################################################
#                                                                                       #
#       README      README      README      README      README      README      README  #
#                                                                                       #
#---------------------------------------------------------------------------------------#
#                                                                                       #
#       This script's purpose is for testing new reports generation with new url.       #
#       If the test is succesful, it will be possible to see the newly                  #
#       generated report on Kibana in Management>Reporting section.                     #
#                                                                                       #
#########################################################################################


if __name__ == "__main__":
    import os
    import json

    # Parameters to for the curl command -u *user:password" H *kibana version*
    params = ' -u kibanaadmin:azerty -H \'kbn-version: 7.6.1\' '

    # To generate the new report using the corresponding url, uncomment the two lines below and paste the url between the quotes
    #test_newReport_url = "''"
    #os.system('curl -X POST' + params + test_newReport_url)