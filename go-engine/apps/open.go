package apps

import (
	"fmt"
	"os/exec"
	"runtime"
	"strings"
)

func Open(name string) error {

	name = strings.ToLower(strings.TrimSpace(name))

	switch runtime.GOOS {

	case "linux":

		apps := map[string]string{
			"notepad":       "gedit",
			"text editor":   "gedit",
			"editor":        "gedit",
			"browser":       "xdg-open",
			"file manager":  "xdg-open",
			"terminal":      "x-terminal-emulator",
			"calculator":    "gnome-calculator",
		}

		command, exists := apps[name]

		if !exists {
			return fmt.Errorf("unknown application: %s", name)
		}

		if command == "xdg-open" {
			return exec.Command(command, ".").Start()
		}

		return exec.Command(command).Start()

	case "windows":

		apps := map[string]string{
			"notepad":      "notepad.exe",
			"text editor":  "notepad.exe",
			"editor":       "notepad.exe",
			"browser":      "start",
			"calculator":   "calc.exe",
			"terminal":     "cmd.exe",
		}

		command, exists := apps[name]

		if !exists {
			return fmt.Errorf("unknown application: %s", name)
		}

		if command == "start" {
			return exec.Command("cmd", "/C", "start", "").Start()
		}

		return exec.Command(command).Start()

	default:

		return fmt.Errorf("unsupported operating system: %s", runtime.GOOS)
	}
}