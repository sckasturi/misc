#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

cd
#unset HISTFILE

PS1='[\u@\h \W]\$ '

function mkpw() { head /dev/urandom | uuencode -m - | sed -n 2p | cut -c1-${1:-30}; }
#export EDITOR="nano"
alias grep='grep --color=auto'
PS1='\[\033[01;31m\]\u\[\033[01;33m\]@\[\033[01;36m\]\h \[\033[01;33m\]\w$(__git_ps1 " \e[0;32m(%s)\e[m") \[\033[01;35m\]$ \[\033[00m\]'
export LESS_TERMCAP_mb=$'\E[01;31m'
export LESS_TERMCAP_md=$'\E[01;31m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;44;33m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;32m'

alias grep='grep --color=auto'
alias egrep='egrep --color=auto'

#export LS_OPTIONS='--human --color=auto'
#alias ls='ls $LS_OPTIONS'
#alias ll='ls $LS_OPTIONS -la'
#alias l='ls $LS_OPTIONS -la'

alias sl='ls -a --human --color=auto'
alias ls='ls --human --color=auto'
alias cd..='cd ..'
alias ..='cd ..'

alias cls='clear'

alias bc='bc -l'

alias ~='cd ~'


#alias weechat='screen -S weechat weechat'
alias cadoth='screen -S cadoth mosh cadoth'


