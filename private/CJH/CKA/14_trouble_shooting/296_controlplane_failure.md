`kubectl get nodes`

`kubectl get pods`

- `service kube-apiserver status`
- `service kube-controller-manager-status`
- `service kube-scheduler status`
- `service kubelet status`
- `service kube-proxy status`

`kubectl logs kube-apiserver-master -n kube-system`

`sudo journalctl -u kube-apiserver`
