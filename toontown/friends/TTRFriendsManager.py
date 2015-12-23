# This file is completely Toontown Rewritten and will be removed later on and recreated from scratch.

from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from otp.otpbase import OTPLocalizer
from toontown.hood import ZoneUtil

class TTRFriendsManager(DistributedObjectGlobal):
    
    def d_removeFriend(self, friendId):
        self.sendUpdate('removeFriend', [friendId])
        
    def d_requestAvatarInfo(self, friendIds):
        self.sendUpdate('requestAvatarInfo', [friendIds])
        
    def d_requestFriendsList(self):
        self.sendUpdate('requestFriendsList', [])
    
    def friendInfo(self, resp):
        base.cr.handleGetFriendsListExtended(resp)
        
    def friendList(self, resp):
        base.cr.handleGetFriendsList(resp)

    def friendOnline(self, id, commonChatFlags, whitelistChatFlags):
        base.cr.handleFriendOnline(id, commonChatFlags, whitelistChatFlags)
        
    def friendOffline(self, id):
        base.cr.handleFriendOffline(id)
                
    def d_getAvatarDetails(self, avId):
        self.sendUpdate('getAvatarDetails', [avId])
        
    def friendDetails(self, avId, inventory, trackAccess, trophies, hp, maxHp, defaultShard, lastHood, dnaString, experience, trackBonusLevel):
        fields = [
            ['setExperience' , experience],
            ['setTrackAccess' , trackAccess],
            ['setTrackBonusLevel' , trackBonusLevel],
            ['setInventory' , inventory],
            ['setHp' , hp],
            ['setMaxHp' , maxHp],
            ['setDefaultShard' , defaultShard],
            ['setLastHood' , lastHood],
            ['setDNAString' , dnaString],
        ]
        base.cr.n_handleGetAvatarDetailsResp(avId, fields=fields)
        
    def d_teleportQuery(self, toId):
        self.sendUpdate('routeTeleportQuery', [toId])
        
    def teleportQuery(self, fromId):
        if not hasattr(base, 'localAvatar'):
            self.sendUpdate('routeTeleportResponse', [ fromId, 0, 0, 0, 0 ])
            return
        if not hasattr(base.localAvatar, 'getTeleportAvailable') or not hasattr(base.localAvatar, 'ghostMode'):
            self.sendUpdate('routeTeleportResponse', [ fromId, 0, 0, 0, 0 ])
            return
        if not base.localAvatar.getTeleportAvailable() or base.localAvatar.ghostMode or base.cr.playGame.getPlaceId() in [10000, 11000, 12000, 13000]:
            if hasattr(base.cr.identifyFriend(fromId), 'getName'):
                base.localAvatar.setSystemMessage(0, OTPLocalizer.WhisperFailedVisit % base.cr.identifyFriend(fromId).getName())
            self.sendUpdate('routeTeleportResponse', [ fromId, 0, 0, 0, 0 ])
            return  

        hoodId = base.cr.playGame.getPlaceId()
        if hasattr(base.cr.identifyFriend(fromId), 'getName'):
            base.localAvatar.setSystemMessage(0, OTPLocalizer.WhisperComingToVisit % base.cr.identifyFriend(fromId).getName())
        self.sendUpdate('routeTeleportResponse', [
            fromId,
            base.localAvatar.getTeleportAvailable(),
            base.localAvatar.defaultShard,
            hoodId,
            base.localAvatar.getZoneId()
        ])
        
    def teleportResponse(self, fromId, available, shardId, hoodId, zoneId):
        base.localAvatar.teleportResponse(fromId, available, shardId, hoodId, zoneId)
        
    def d_whisperSCTo(self, toId, msgIndex):
        self.sendUpdate('whisperSCTo', [toId, msgIndex])
        
    def setWhisperSCFrom(self, fromId, msgIndex):
        if not hasattr(base, 'localAvatar'):
            return
        if not hasattr(base.localAvatar, 'setWhisperSCFrom'):
            return
        base.localAvatar.setWhisperSCFrom(fromId, msgIndex)
        
    def d_whisperSCCustomTo(self, toId, msgIndex):
        self.sendUpdate('whisperSCCustomTo', [toId, msgIndex])
      
    def setWhisperSCCustomFrom(self, fromId, msgIndex):
        if not hasattr(base, 'localAvatar'):
            return
        if not hasattr(base.localAvatar, 'setWhisperSCCustomFrom'):
            return
        base.localAvatar.setWhisperSCCustomFrom(fromId, msgIndex)
        
    def d_whisperSCEmoteTo(self, toId, emoteId):
        self.sendUpdate('whisperSCEmoteTo', [toId, emoteId])
        
    def setWhisperSCEmoteFrom(self, fromId, emoteId):
        if not hasattr(base, 'localAvatar'):
            return
        if not hasattr(base.localAvatar, 'setWhisperSCEmoteFrom'):
            return
        base.localAvatar.setWhisperSCEmoteFrom(fromId, emoteId)
        
    def receiveTalkWhisper(self, fromId, message):
        toon = base.cr.identifyAvatar(fromId)
        if toon:
            base.localAvatar.setTalkWhisper(fromId, 0, toon.getName(), message, [], 0)
