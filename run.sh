#!/usr/bin/env bash

python3 webcam.py &
WEBCAM_PID=$!

python3 botext.py &
BOT_PID=$!

cat > stop.sh << EOF
#!/usr/bin/env bash
kill $WEBCAM_PID
kill $BOT_PID
EOF

echo 'started! Run stop.sh to stop'
