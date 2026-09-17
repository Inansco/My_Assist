package apps

import (
	"os/exec"
	"runtime"
)

func Open(name string) error {
	var cmd *exec.Cmd

	switch runtime.GOOS {
	case "windows":
		cmd = exec.Command("cmd", "/C", "start", "", name)
	default:
		cmd = exec.Command(name)
	}

	return cmd.Start()
}

