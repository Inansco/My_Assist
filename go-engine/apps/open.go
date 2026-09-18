package apps

import (
	"os/exec"
	"runtime"
	"strings"
)

func Open(name string) error {

	name = strings.TrimSpace(name)

	switch runtime.GOOS {

	case "windows":

		cmd := exec.Command(
			"cmd",
			"/C",
			"start",
			"",
			name,
		)

		return cmd.Start()

	default:

		// Linux application names are usually lowercase.
		name = strings.ToLower(name)

		cmd := exec.Command(name)

		return cmd.Start()
	}
}