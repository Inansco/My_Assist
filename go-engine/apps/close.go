package apps

import (
	"fmt"
	"os/exec"
	"runtime"
	"strings"
)

func Close(name string) error {

	name = strings.TrimSpace(name)

	switch runtime.GOOS {

	case "windows":

		cmd := exec.Command(
			"taskkill",
			"/IM",
			fmt.Sprintf("%s.exe", name),
			"/F",
		)

		return cmd.Run()

	case "linux":

    name = strings.ToLower(name)

    cmd := exec.Command(
        "pkill",
        name,
    )

    return cmd.Run()

	default:

		return fmt.Errorf("unsupported operating system")
	}
}
