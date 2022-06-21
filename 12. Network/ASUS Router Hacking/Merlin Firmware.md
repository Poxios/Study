# Merlin Firmware
* https://www.asuswrt-merlin.net/download

```
Here's how I did it.
You will need Putty, WinSCP, CFEEdit or other hex editor, asus rt-ac68 firmware & mtd-write. * See PS#4 note below*
If you search for "Bay area tech pros" in Google you can find the files.

1. Enable SSH in "Adminitration" - "System" tab.

2. Open Putty and WinSCP and connect them to your router using its Lan ip address. In WinSCP selet SCP as protocol.

3. In putty type:
cat /dev/mtd0 > original_cfe.bin

4. In WinSCP you should be in the /home/root or /root directory hit the refresh icon on right side to see original_cfe.bin.

5. Copy original_cfe.bin form router to your computer by dragging from the right window to your computer in the left window.

6. Open the original_cfe.bin in your editor and find the 2 instances of RT-AC56U and replace with RT-AC68U save the file as new_cfe.bin

7. In WinSCP copy the new_cfe.bin, mtd-write, and RT-AC68U_3.0.0.4_384_45149-g467037b.trx (or any ASUS firmware) back to your router.

8. In Putty type: chmod u+x mtd-write

9. In Putty type: ./mtd-write new_cfe.bin boot

10. In Putty type: mtd-write2 RT-AC68U_3.0.0.4_384_45149-g467037b.trx linux (or whatever firmware you are using)

11. Follow steps below to perform NVRAM Reset, wait for reboot <5 mins
a. Power off router
b. Wait 10 seconds
c. Press and hold WPS button *See PS#2 note below*
d. Power up the router and continue to hold WPS button for 15-20 seconds until power LED starts blinking very quickly.

After reboot it should report as a rt-ac68u.

PS#1 Since initially writing this I uploaded a rt-ac68u official .cfe to it with the correct mac addresses and secret code and it works fine except the WAN is still LAN1 and the power light is the only light that lights up.

PS#2 From Asusfan999 "Instead of messing with the WPS button and the switch, I found that the command line incantation "mtd-erase2 nvram" followed by "reboot" was much more convenient."

PS#3 The USB port does not work unless an AC68u cfe is uploaded to the router as discussed later in the posting.

PS#4 Asusfan9999 reported having better luck with "mtd-write v2" (executable size 733,422) Google to find it.
```