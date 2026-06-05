# 1. Common Issues & Solutions
#（英文作业专用，真实、合理、不夸张）

## Issue 1: Ansible ping failed / SSH connection refused
**Problem**:
When running `ansible all -m ping`, the command fails with “Host unreachable”, “Connection timed out”, or “Permission denied”.

**Solution**:
- Check that VM public IPs are correct in `inventory.ini`.
- Ensure the SSH private key path matches `ansible_ssh_private_key_file`.
- Verify the cloud security group allows inbound SSH (port 22) and HTTP (port 80).
- Test manual SSH first: `ssh ubuntu@<ip>`. If SSH works, Ansible works.

## 2: Nginx failed to start / invalid configuration
**Problem**:
After running `lb.yml`, Nginx returns an error such as “directive not allowed” or “invalid upstream”.

**Solution**:
- Check indentation in the Nginx configuration inside `lb.yml`.
- Ensure real IP addresses of `web-1` and `web-2` are used, not placeholders.
- Run `nginx -t` inside the load balancer to debug syntax errors.

## Issue 3: Load balancer shows only one web server
**Problem**:
When refreshing `http://<lb-1-ip>`, only `web-1` or `web-2` appears.

**Solution**:
- Clear browser cache or use `curl` multiple times.
- Check that both web servers are running and reachable from `lb-1`.
- Verify the `upstream` block in Nginx contains both backend IPs.

## Issue 4: Permission denied when using become: true
**Problem**:
Ansible cannot install packages because of insufficient privileges.

**Solution**:
- Ensure `become: true` is present in the playbook.
- Confirm the `ubuntu` user has sudo access on target VMs.

---

# 2. Full English Lab Report（可直接提交）
# Lab Report: Automating Multiple Servers with Ansible

## 1. Objective
The goal of this lab is to automate the configuration of multiple web servers and a load balancer using Ansible. By the end, we will have two Nginx web servers and one Nginx load balancer that distributes client traffic between them.

## 2. Equipment & Environment
- 3 Ubuntu 24.04 virtual machines in Yandex Cloud:
  - web-1
  - web-2
  - lb-1
- Local control node with Ansible installed (WSL2 / Linux)
- SSH key authentication for remote access
- Public IP addresses for all instances

## 3. Topology
```
Client → lb-1 (load balancer) → web-1 / web-2
```

## 4. Workflow Summary
1. Prepare the control node and install Ansible.
2. Create three cloud VMs and test SSH connectivity.
3. Create an inventory file to define target hosts.
4. Write a playbook to automatically install and configure Nginx on web servers.
5. Write a playbook to set up Nginx as a load balancer.
6. Run playbooks and verify traffic distribution.

## 5. Implementation Details

### Inventory Configuration
The `inventory.ini` file defines the group of web servers and the load balancer, along with SSH credentials and connection settings.

### Web Server Playbook
The `web.yml` playbook:
- Installs Nginx
- Creates a custom HTML page showing the hostname
- Starts and enables the Nginx service

### Load Balancer Playbook
The `lb.yml` playbook:
- Installs Nginx
- Configures an upstream backend with two web servers
- Sets up reverse proxy for load balancing
- Validates configuration and restarts Nginx

## 6. Results
After running the playbooks:
- Both web-1 and web-2 serve unique web pages.
- The load balancer distributes requests between the two backends.
- Refreshing the page shows alternating responses from each web server.
- All configurations are applied automatically without manual server login.

## 7. Issues Encountered & Solutions
- **SSH connection failure**: Fixed by verifying security groups, IP addresses, and private key path.
- **Nginx configuration error**: Fixed by correcting indentation and replacing placeholder IPs.
- **Load balancing not working**: Fixed by checking upstream servers and testing backend reachability.

## 8. Conclusion
This lab successfully demonstrated server automation using Ansible. Instead of manually configuring each machine, we defined infrastructure as code and applied configurations in a consistent, repeatable way. The load balancer efficiently distributes traffic, improving availability and scalability. This method is widely used in real DevOps and system administration.


