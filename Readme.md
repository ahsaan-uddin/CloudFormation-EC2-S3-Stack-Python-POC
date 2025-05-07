**Objective Overview![ref1]**

This Proof of Concept POC is designed to demonstrate infrastructure automation and cloud-native resource management using AWS services. The deliverables include:

- A CloudFormation YAML template.
- A Launch Stack URL.
- A secure Python script (no hardcoded credentials).
- Documentation for implementation and execution.![ref2]

📁 **Required Deliverables**

 CloudF ormation YAML file ( template.yaml )  CloudF![](Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.003.png) ormation Stack Launch URL

 Python script (using IAM role/profile)

 This implement ation documentation![](Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.004.png)

🛠 **Implementation Steps**

1. **Design CloudFormation Template**

Create a YAML file that describes the AWS resources to be deployed. For this task:

- Include an **S3 bucket** (with read-only access).
- Include an **EC2 instance** (e.g., Amazon Linux).
- Define outputs to easily reference the resource IDs (e.g., bucket name, instance ID.

  📝 Use descr iptive logic al IDs, t ags, and output s to keep ![ref3]resources well-organized and queryable.![ref2]

2. **Host the Template Publicly**

To generate a CloudFormation Launch URL, the template must be hosted at a public HTTPS-accessible URL.

Options include:

- **GitHub** Upload to a public repository and use the **raw** file URL.
- **S3 bucket** Upload with public-read permission and enable HTTPS access.![ref2]
3. **Generate the Launch Stack URL**

Use the following format to generate a CloudFormation launch link:

https://console.aws.amazon.com/cloudformation/home?#/stacks/create/re view?templateURL=<public-template-url>![](Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.006.png)

Replace  <public-template-url> with the actual URL of your hosted  template.yaml . This URL will allow anyone with AWS Console access to quickly launch the 

stack in their account.![ref4]

4. **Develop the Python Automation Script**

Create a Python script that:

- Accepts the **CloudFormation Launch URL** as input.
- Extracts the  templateURL parameter.
- Uses the AWS SDK Boto3 to:
  - Create a new CloudFormation stack.
  - Wait for the stack to complete creation.
  - Retrieve inventory information like:
    - EC2 instance IDs
    - S3 bucket names
- Does **not** use any hardcoded keys or ARNs.

  🛡 The scr ipt should assume that it is running with pr oper ![ref3]IAM permissions (via EC2 instance profile or assumed role).![ref2]

5. **Run & Verify the Solution**

To test your implementation:

 **Ensure AWS CLI is configured** with assumed role or IAM profile (no manual 

credentials).

 **Execute the script** in an environment with required IAM permissions.  **Verify the resources** have been created in the AWS Console.

 **Check scr ipt output** to confirm inventory fetch is accurate.![ref1]

✅ **Best Practices Followed**

- **Security** No credentials hardcoded; uses environment-based IAM access.
- **Modular approach** Clear logical separation of steps.
- **Clarity** Well-commented and documented for review or reuse.
- **Reusability** Stack and script can be reused with minor changes.![ref4]
Objectiv e Ov erview 3

[ref1]: Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.001.png
[ref2]: Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.002.png
[ref3]: Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.005.png
[ref4]: Aspose.Words.1d38e62f-facd-4efe-9b45-366d7699af34.007.png
