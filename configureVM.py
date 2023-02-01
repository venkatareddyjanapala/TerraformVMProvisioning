import subprocess
import sys
terraformInit = subprocess.run(["/usr/local/bin/terraform","init"])
print("The Terraform exit code was: %d" % terraformInit.returncode)
if terraformInit.returncode == 0:
  terraformplan = subprocess.run(["/usr/local/bin/terraform","plan"])
  print("The Terraform plan exit code was: %d" % terraformplan.returncode)
  if terraformplan.returncode == 0:
        terraformautoApprove = subprocess.run(["/usr/local/bin/terraform","apply","-auto-approve"])
        print("The Terraform approve exit code was: %d" % terraformautoApprove.returncode)
        if terraformautoApprove.returncode == 0:
            print("The Terraform Auto approve exit code was: %d" % terraformautoApprove.returncode)
        else:
            sys.exit("The Terraform Auto approve exit code was: %d" % terraformautoApprove.returncode)
  else:
      sys.exit("The Terraform plan exit code was: %d" % terraformplan.returncode)
else:
    print("terraform initialisation failed")