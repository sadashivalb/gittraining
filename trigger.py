import requests
joburl = 'http://localhost:6789/job/sada/build?token=sada' #If the remote job not taking arguments
st = requests.get(joburl,verify=False)
print st
if st.status_code == 200:
    print "Hmm"

pjoburl = "http://localhost:6789/job/sada/buildWithParameters?token=sada&param1=paramvalue" #If the remote job taking arguments
st = requests.get(pjoburl)
if st.status_code == 200:
    print "Hmm"
