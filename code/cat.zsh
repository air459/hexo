cat() {
  /bin/clear
  F11="$(PYRUN $PS/F11/main.py !)"
  if [ $# -eq 0 ]; then
    if [[ $F11 == "False" ]]; then
      /usr/bin/xdotool key F11
    fi
    /usr/bin/fastfetch
  else
    /bin/cat "$@"
  fi
}
