#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Dec 12, 2020 09:07:43 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1299x787+343+122
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Login Page"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    frame $top.fra51 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 755 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 1291 
    vTcl:DefineAlias "$top.fra51" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra51
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #c0c0c0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {USER ID :} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #c0c0c0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {PASSWORD :} 
    vTcl:DefineAlias "$site_3_0.lab53" "Label3" vTcl:WidgetProc "Toplevel1" 1
    text $site_3_0.tex54 \
        -background white -font TkTextFont -foreground black -height 45 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 359 -wrap word 
    $site_3_0.tex54 configure -font "TkTextFont"
    $site_3_0.tex54 insert end text
    vTcl:DefineAlias "$site_3_0.tex54" "useridtb" vTcl:WidgetProc "Toplevel1" 1
    text $site_3_0.tex55 \
        -background white -font TkTextFont -foreground black -height 44 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 254 -wrap word 
    $site_3_0.tex55 configure -font "TkTextFont"
    $site_3_0.tex55 insert end text
    vTcl:DefineAlias "$site_3_0.tex55" "Text1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground #f9f9f9 -activeforeground black -background #0000ff \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {PLEASE LOGIN...!} 
    vTcl:DefineAlias "$site_3_0.lab56" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text LOGIN 
    vTcl:DefineAlias "$site_3_0.but58" "loginbtn" vTcl:WidgetProc "Toplevel1" 1
    text $site_3_0.tex59 \
        -background white -font TkTextFont -foreground black -height 46 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 353 -wrap word 
    $site_3_0.tex59 configure -font "TkTextFont"
    $site_3_0.tex59 insert end text
    vTcl:DefineAlias "$site_3_0.tex59" "passwordtb" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -background #00ff00 -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -text {WELCOME TO AUTOMATIC EXAM FORM FILLER} 
    vTcl:DefineAlias "$site_3_0.lab45" "Label2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.234 -y 0 -rely 0.368 -width 0 \
        -relwidth 0.16 -height 0 -relheight 0.064 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -relx 0.234 -y 0 -rely 0.518 -width 0 \
        -relwidth 0.157 -height 0 -relheight 0.064 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tex54 \
        -in $site_3_0 -x 0 -relx 0.435 -y 0 -rely 0.368 -width 0 \
        -relwidth 0.278 -height 0 -relheight 0.06 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tex55 \
        -in $site_3_0 -x 0 -relx 0.971 -y 0 -rely 1.038 -width 0 \
        -relwidth 0.336 -height 0 -relheight 0.183 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.363 -y 0 -rely 0.218 -width 0 \
        -relwidth 0.229 -height 0 -relheight 0.064 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but58 \
        -in $site_3_0 -x 0 -relx 0.419 -y 0 -rely 0.695 -width 136 \
        -relwidth 0 -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tex59 \
        -in $site_3_0 -x 0 -relx 0.435 -y 0 -rely 0.518 -width 0 \
        -relwidth 0.273 -height 0 -relheight 0.06 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.331 -y 0 -rely 0.054 -width 0 \
        -relwidth 0.286 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra51 \
        -in $top -x 0 -relx 0.022 -y 0 -rely 0.037 -width 0 -relwidth 0.955 \
        -height 0 -relheight 0.933 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
