# CUDA

## CUDA 7.5 installation steps <a id="cuda_75_installation_steps"></a>

0\) Download your relevant CUDA.run file: mine was: cuda\_7.0.28\_linux.run Note, that once again this install is if you purely want to use your graphics card \(Titan X\) for GPU/CUDA purposes and not for rendering.

Also run: 

```bash
sudo apt-get install build-essential
```

1\) I start off with the regular GUI and Ubuntu working with no login problems. 2\) No need to create an xorg.conf file. If you have one, remove it \(assuming you ahve a fresh OS install\). $ sudo rm /etc/X11/xorg.conf

3\) Create the /etc/modprobe.d/blacklist-nouveau.conf file with : blacklist nouveau option nouveau modeset=0

Then $sudo update-initramfs -u

4\) Reboot computer. Nothing should have changed in loading up menu. You should be taken to the login screen. Once there type: Ctrl + Alt + F1, and login to your user. 5\) Go to the directory where you have the CUDA driver, and run $chmod a+x . 7\) Now, run $ sudo service lightdm stop The top line is a necessary step for installing the driver. 8\) I run the CUDA driver run file. \*Notice that I explicitly don't want the OpenGL flags to be installed: $ sudo bash cuda-7.0.28\_linux.run –no-opengl-libs

9\) During the install: Accept EULA conditions Say YES to installing the NVIDIA driver SAY YES to installing CUDA Toolkit + Driver Say YES to installing CUDA Samples

Say NO rebuilding any Xserver configurations with Nvidia.

10\) Installation should be complete. Now check if device nodes are present: Check if /dev/nvidia\* files exist. If they don't, do : $ sudo modprobe nvidia

11\) Set Environment path variables: $ export PATH=/usr/local/cuda-7.0/bin:$PATH $ export LD\_LIBRARY\_PATH=/usr/local/cuda-7.0/lib64:$LD\_LIBRARY\_PATH

\*Change depending on your cuda version.

12\) Verify the driver version: $ cat /proc/driver/nvidia/version

13\) Check CUDA driver version: $ nvcc -V

\[Optional\] At this point you can switch the lightdm back on again by doing: $ sudo service lightdm start.

You should be able to login to your session through the GUI without any problems or login-loops.

14\) Create CUDA Samples. Go to your NVIDIA\_CUDA-7.5\_Samples folder and type $make.

15\) Go to NVIDIA\_CUDA-7.5\_Samples/bin/x86\_64/linux/release/ for the demos, and do the two standard checks: ./deviceQuery to see your graphics card specs and ./bandwidthTest to check if its operating correctly.

Both tests should ultimately output a 'PASS' in your terminal.

16\) Reboot. Everything should be ok.Edit

### Reference <a id="reference"></a>

[https://devtalk.nvidia.com/default/topic/878117/-solved-titan-x-for-cuda-7-5-login-loop-error-ubuntu-14-04-/](https://devtalk.nvidia.com/default/topic/878117/-solved-titan-x-for-cuda-7-5-login-loop-error-ubuntu-14-04-/)

