## Environment
- Linux Ubuntu LTS 22.04 Jammy jelly fish
- AMD ryzen 5 5600H

## Output of `kubectl get pods,svc`

```bash
$ kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/devops-labs-5f58bb6654-7f2rr   1/1     Running   0          12m

NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/devops-labs   LoadBalancer   10.106.220.144   <pending>     5000:30968/TCP   11m
service/kubernetes    ClusterIP      10.96.0.1        <none>        443/TCP          26m

```

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab9_submission/k8s/images/lab9.1.png)



## Output of `minikube service --all`

```bash
$ minikube service --all
|-----------|------|-------------|-----------------------------|
| NAMESPACE | NAME | TARGET PORT |             URL             |
|-----------|------|-------------|-----------------------------|
| default   | app  |        5000 | http://192.168.59.100:31591 |
|-----------|------|-------------|-----------------------------|
|-----------|---------------------------|-------------|-----------------------------|
| NAMESPACE |           NAME            | TARGET PORT |             URL             |
|-----------|---------------------------|-------------|-----------------------------|
| default   | devops-lab-app-deployment |        5000 | http://192.168.59.100:32345 |
|-----------|---------------------------|-------------|-----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app in default browser...
🎉  Opening service default/devops-lab-app-deployment in default browser...
```

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab9_submission/k8s/images/lab9.3.png)


## Browser screenshot

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab9_submission/k8s/images/lab9.2.png)