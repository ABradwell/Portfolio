
!create ottawaRace:Race
!set ottawaRace.location:= 'Calabogie Peak'


!create theWall:Team
!set theWall.name:= 'TheWall'

!create trump:Member
!create scheer:Member
!create maduro:Member
!create bin:Member

!set trump.firstName:= 'Trump'
!set scheer.firstName:= 'Scheer'
!set maduro.firstName:= 'Maduro'
!set bin.firstName:= 'Bin'

!insert (trump,theWall) into recruits
!insert (scheer,theWall) into recruits
!insert (maduro,theWall) into recruits
!insert (bin,theWall) into recruits

!insert (theWall,trump) into isUsing
!insert (theWall,scheer) into isUsing
!insert (theWall,maduro) into isUsing
!insert (theWall,bin) into isUsing

!insert (theWall, ottawaRace) into participates


!create peaceTeam:Team
!set peaceTeam.name:= 'PeaceTeam'

!create putin:Member
!create bush:Member
!create saddam:Member
!create pinochet:Member

!create ford:Member
!create reagan:Member
!create kim:Member


!set putin.firstName:= 'Putin'
!set bush.firstName:= 'Bush'
!set saddam.firstName:= 'Saddam'
!set pinochet.firstName:= 'Pinochet'
!set ford.firstName:= 'Ford'
!set reagan.firstName:= 'Reagan'
!set kim.firstName:= 'Kim'


!insert (putin,peaceTeam) into recruits
!insert (bush,peaceTeam) into recruits
!insert (saddam,peaceTeam) into recruits
!insert (pinochet,peaceTeam) into recruits
!insert (ford,peaceTeam) into recruits
!insert (reagan,peaceTeam) into recruits
!insert (kim,peaceTeam) into recruits

!insert (peaceTeam, putin) into isUsing
!insert (peaceTeam, bush) into isUsing
!insert (peaceTeam, saddam) into isUsing
!insert (peaceTeam, pinochet) into isUsing


!insert (peaceTeam, ottawaRace) into participates


!create amigos:Team
!set amigos.name:= 'Amigos'

!create obama:Member
!create nixon:Member
!create trudeau:Member
!create macron:Member
!create chirac:Member


!set obama.firstName:= 'Putin'
!set nixon.firstName:= 'Bush'
!set trudeau.firstName:= 'Saddam'
!set macron.firstName:= 'Pinochet'
!set chirac.firstName:= 'Ford'



!insert (obama,amigos) into recruits
!insert (nixon,amigos) into recruits
!insert (trudeau,amigos) into recruits
!insert (macron,amigos) into recruits
!insert (chirac,amigos) into recruits

!insert (amigos,obama) into isUsing
!insert (amigos,nixon) into isUsing
!insert (amigos,trudeau) into isUsing
!insert (amigos,macron) into isUsing


!insert (amigos, ottawaRace) into participates


!create leg1:Leg
!create leg2:Leg
!create leg3:Leg
!create leg4:Leg

!create biking:Skill
!create climbing:Skill
!create obstacles:Skill
!create swimming:Skill
!create kayaking:Skill
!create running:Skill

!set biking.type:= 'Biking'
!set climbing.type:= 'Climbing'
!set obstacles.type:= 'Obstacles'
!set swimming.type:= 'Swimming'
!set kayaking.type:= 'Kayaking'
!set running.type:= 'Running'

!insert (biking, leg1) into involves
!insert (climbing, leg2) into involves
!insert (obstacles, leg2) into involves
!insert (swimming, leg3) into involves
!insert (kayaking, leg3) into involves
!insert (running, leg4) into involves


!insert (leg1, ottawaRace) into contains
!insert (leg2, ottawaRace) into contains
!insert (leg3, ottawaRace) into contains
!insert (leg4, ottawaRace) into contains

