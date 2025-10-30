from aci_session import AciSession
import requests

requests.packages.urllib3.disable_warnings()

session = AciSession("https://sandboxapicdc.cisco.com", "admin", "ciscopsdt")
session.login()

tenant_name = "VSCode_Lab_Tenant"
url = f"{session.apic_url}/api/mo/uni/tn-{tenant_name}.json"
payload = {
  "fvTenant": {"attributes": {"name": tenant_name, "descr": "Created via VS Code Python script"}}
}

response = requests.post(url, json=payload, cookies=session.cookies, verify=False)
print(f"[+] Created tenant {tenant_name}, status: {response.status_code}")