package apps

import (
	"fmt"
	"os/exec"
	"runtime"
)

func Close(name string) error {

	switch runtime.GOOS {

	case "windows":

		cmd := exec.Command(
			"taskkill",
			"/IM",
			fmt.Sprintf("%s.exe", name),
			"/F",
		)

		return cmd.Run()

	default:

		return fmt.Errorf("unsupported operating system")
	}
}