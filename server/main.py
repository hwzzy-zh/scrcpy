import asyncio
import signal


async def start_scrcpy():
    exe = r"scrcpy.exe"
    cmd = f'{exe}  --no-playback --no-window --record=file.mp4'
    proc = await asyncio.create_subprocess_shell(cmd)
    await asyncio.sleep(5)
    proc.send_signal(signal.CTRL_C_EVENT)
    return proc

if __name__ == '__main__':
    asyncio.run(start_scrcpy())
