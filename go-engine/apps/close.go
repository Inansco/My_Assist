package apps

import (
	"fmt"
	"os/exec"
	"runtime"
	"strings"
)

func Close(name string) error {

	name = strings.ToLower(strings.TrimSpace(name))

	switch runtime.GOOS {

	case "linux":

		apps := map[string]string{
			"notepad":      "gedit",
			"text editor":  "gedit",
			"editor":       "gedit",
			"browser":      "firefox",
			"terminal":     "gnome-terminal",
			"calculator":   "gnome-calculator",
		}

		process, exists := apps[name]

		if !exists {
			return fmt.Errorf("unknown application: %s", name)
		}

		return exec.Command("pkill", "-f", process).Run()

	case "windows":

		apps := map[string]string{
			"notepad":      "notepad.exe",
			"text editor":  "notepad.exe",
			"editor":       "notepad.exe",
			"browser":      "chrome.exe",
			"terminal":     "cmd.exe",
			"calculator":   "calc.exe",
		}

		process, exists := apps[name]

		if !exists {
			return fmt.Errorf("unknown application: %s", name)
		}

		return exec.Command(
			"taskkill",
			"/IM",
			process,
			"/F",
		).Run()

	default:

		return fmt.Errorf("unsupported operating system: %s", runtime.GOOS)
	}
}