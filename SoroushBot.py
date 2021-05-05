from client import Client
import os
from os.path import getsize
import ntpath
from moviepy.editor import VideoFileClip

class SoroushBot:

    def __init__(self, bot_token):
        global b
        b= Client(bot_token)

    def sendText(self,target_id,caption):
        resualt=b.send_text(target_id,caption)
        #resualt=[error,success]
        return resualt
        
    def imageVideoResalotion(self,path):
        clip=VideoFileClip(path)
        width  = int(round(clip.w))
        height = int(round(clip.h))
        return [width,height]

    def sendImage(self,target_id,image_path,image_thumbnail_path,caption):
        rImage=b.upload_file(image_path)
        #rImage=[image_error, image_url]

        if rImage[1]:
            rThumb = b.upload_file(image_thumbnail_path)
            #rThumb=[thumbnail_error, thumbnail_url]
            scale=self.imageVideoResalotion(image_path)

            resualt = b.send_image(target_id, rImage[1],
                                          ntpath.basename(image_path),
                                          getsize(image_path), scale[0], scale[1],
                                          rThumb[1],
                                          caption)
            #if(resualt[1] != 'OK'):
            #    print("paramets that gotten this function",image_path,image_thumbnail_path,caption)            
            return resualt
        
        else :
            #if(rImage[1] != 'OK'):
            #    print("paramets entered for this function",image_path,image_thumbnail_path,caption)
            return rImage


    def sendVideo(self,target_id,video_path,video_thumbnail_path,caption,durationSeconds=None):
        rVideo=b.upload_file(video_path)
        #rVideo=[video_error, video_url]

        if rVideo[1]:
            rThumb= b.upload_file(video_thumbnail_path)
            #rThumb=[thumbnail_error, thumbnail_url]
            
            if (durationSeconds==None):
                clip=VideoFileClip(video_path)
                durationSeconds=int(round(clip.duration))
                
            scale=self.imageVideoResalotion(video_path)#[width,height]

            resualt= b.send_video(target_id, rVideo[1],
                                    ntpath.basename(video_path),
                                    getsize(video_path),
                                          durationSeconds*1000, scale[0], scale[1],
                                          rThumb[1],
                                          caption)
            #if(resualt[1] != 'OK'):
            #    print("paramets that gotten this func",video_path,video_thumbnail_path,caption,durationSeconds)
            return resualt

        else:
            #if(rVideo[1] != 'OK'):
            #    print("paramets entered for this func",video_path,video_thumbnail_path,caption,durationSeconds)
            return rVideo


    def sendFile(self,target_id,file_path,caption):
        rFile = b.upload_file(file_path)
        #rFile=[error, file_url]

        resualt = b.send_attachment(target_id, rFile[1], ntpath.basename(file_path),
                                            getsize(file_path),
                                            caption)
        return resualt

    def sendLocation(self,target_id, latitude, longitude, caption='', keyboard=None):
        resualt=b.send_location(target_id, latitude, longitude, caption, keyboard)

        return resualt
    
    def sendAudio (self, target_id, audio_path, caption, audio_duration):
        audioUrl=b.upload_file(audio_path)
        
        audiotype = 'PUSH_TO_TALK'
        extra_params = {
            'fileDuration': audio_duration*1000
        }

        resualt = b.send_file(target_id, caption,
                                 ntpath.basename(audio_path), audiotype,
                                 audioUrl[1], getsize(audio_path),
                                extra_params)

        return resualt
