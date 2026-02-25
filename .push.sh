if [ "$1" = "s" ]; then
  git add .
  git commit -m "$(date)"
  git push -u origin source
elif [ "$1" = "h" ]; then
  hexo d
  hexo g
elif [ "$1" = "z" ]; then
  git add .
  git commit -m "$(date)"
  git push -u origin source
  hexo d
  hexo g
fi
