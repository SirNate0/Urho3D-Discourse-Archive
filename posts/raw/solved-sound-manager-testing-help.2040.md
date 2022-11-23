vivienneanthony | 2017-01-02 01:12:29 UTC | #1

Hi,

I'm trying to make a sound manager. So far it plays music but the frequency seems off which is not playing at the right rate.. I'm not sure what is wrong.

Vivienne

[code]
#include "CubeOpenBoxClientStd.h"

#include "AlphaEngine/Database/AlphaDatabase.h"

#include "AlphaEngine/GameLogic/BaseGameLogic.h"
#include "AlphaEngine/EventManager/Event/Server/ServerEvent.h"
#include "AlphaEngine/EventManager/Event/Client/ClientEvent.h"
#include "AlphaEngine/EventManager/Event/Request/RequestEvent.h"

#include "AlphaEngine/GameLogic/PlayerManager/HeroManager/HeroManager.h"
#include "SoundManager.h"

bool SoundManager::m_bIsInstantiated = false;

SoundManager::SoundManager(Context* context) : Object(context)
    ,m_bInitialized(false)
    ,m_bCurrentSound(0)
    ,m_pScene(NULL)
{
    // Fail if want to construct more than one SoundManager
    assert(!m_bIsInstantiated);

    // Flag generated
    m_bIsInstantiated = true;

    // Set defaults - not need but to be safe;
    m_bInitialized=false;
    m_bCurrentSound=0;
    m_pScene=NULL;

    // Get the game logic
    m_pGameLogic = g_pApp->GetGameLogic();
    m_pAudio = g_pApp->GetSubsystem<Audio>();

    return;
}

SoundManager::~SoundManager()
{
    // Prototype
    // Stop all sounds
    m_pAudio->Stop();

    return;
}

// Initialize
bool SoundManager::Initialize(void)
{
    // Initialize Delegates
    InitializeAllDelegates();

    // Initialize Sound SOurce
    m_pSoundSource = new SoundSource(context_);

    // Set source type
    m_pSoundSource->SetSoundType(SOUND_MUSIC);

    // Add sound source
    m_pAudio->AddSoundSource(m_pSoundSource);

    // Stop all sounds
    m_pAudio->Stop();

    // Set Initialize state to true
    m_bInitialized = true;

    // Master Gain
    m_pAudio->SetMasterGain(SOUND_MUSIC, 1.0f);
    m_pAudio->SetMasterGain(SOUND_EFFECT,1.0f);

    return true;
}

// Initialize all delegates
void SoundManager::InitializeAllDelegates(void)
{
    return;
}

// Handle VUpdate
void SoundManager::VOnUpdate(float timeStep)
{

    if(!m_bInitialized&&!m_bIsInstantiated)
    {
        //   ALPHAENGINE_LOGINFO("Not Initialized");
        return;
    }

    if(m_bUpdating||!m_pScene)
    {
        return;
    }

    // Is Playing
    if(m_bIsPlaying)
    {
        if(!m_pSoundSource->IsPlaying())
        {
            // if sounds exist
            if(m_Sounds.Size()>0)
            {
                // increase current sound
                m_bCurrentSound++;

                // if sound is above loaded sounds
                if(m_bCurrentSound>=m_Sounds.Size())
                {
                    // play first sound
                    m_bCurrentSound=0;
                }

                // Play Sound
                m_pSoundSource->Play(m_Sounds.At(m_bCurrentSound).SoundPtr,m_Sounds.At(m_bCurrentSound).SoundFrequency);
            }
        }
    }
}


bool SoundManager::LoadSoundType(String type, bool reset = true)
{
    FileSystem * fileSystem = g_pApp->GetFileSystem();

    // load from path
    XMLFile* file = g_pApp->GetConstantResCache()->GetResource<XMLFile>("Sounds/Sounds.xml");

    if (!file)
    {
        URHO3D_LOGERROR("Failed to load hero data from xml file");
        return false;
    }

    //Get Root
    XMLElement root = file->GetRoot();

    // stop all Sound
    m_bIsPlaying = false;
    m_bUpdating = true;

    // Verify first child
    if (root)
    {
        // Get a sound node
        XMLElement NextNode = root.GetChild("Sound");

        // Test each one
        do
        {
            // Test if a type exist and path
            XMLElement TypeNode = NextNode.GetChild("Type");
            XMLElement PathNode = NextNode.GetChild("Path");
            XMLElement FrequencyNode = NextNode.GetChild("Frequency");

            // if type is not null and path
            if(TypeNode.NotNull()&&PathNode.NotNull())
            {
                // Get the type node
                String typestring=TypeNode.GetAttribute("value");
                String soundpath = PathNode.GetAttribute("value");

                // if type string contains type
                if(typestring.Contains(type, false)&&!soundpath.Empty())
                {
                    // create a file path
                    String fullpath = g_pApp->GetGameDataDirectory()+"/"+soundpath;

                    // continue
                    if(fileSystem -> FileExists(fullpath))
                    {
                        // get frequency
                        float frequency = 44100.0f;

                        // if freequency not there use 44.1 as the default
                        if(FrequencyNode.NotNull())
                        {
                            frequency = FrequencyNode.GetFloat("value");
                        }

                        // load resource
                        Sound * newSound = g_pApp->GetConstantResCache()->GetResource<Sound>(soundpath);

                        // Set sound looped
                        newSound->SetLooped(false);

                        // push new sound
                        if(newSound)
                        {
                            // Add sound a default frequency
                            m_Sounds.Push({newSound, newSound->GetFrequency()});
                        }
                    }
                    else
                    {
                        ALPHAENGINE_LOGINFO(fullpath);
                    }
                }
            }
        }
        while(NextNode =  NextNode.GetNext("Sound"));
    }

    // Reset Updating
    m_bUpdating = false;


    return true;
}

bool SoundManager::SetScene(Scene * setscene)
{
    // Set Scene
    m_pScene = setscene;

    // Add Music Node
    m_pMusicNode = m_pScene -> CreateChild("Music");
    m_pMusicNode->AddComponent(m_pSoundSource,0, LOCAL);

}


bool SoundManager::Play(void)
{
    if(!m_bInitialized||!m_pScene||m_bIsPlaying||m_bUpdating)
    {
        // Error message
        ALPHAENGINE_LOGINFO("Error Occurred");

        return false;
    }

    if(m_Sounds.Size()>0)
    {
        // play
        m_pAudio->Play();

        // Reset sounds to 0
        m_bCurrentSound = 0;

        // Sound
        m_pSoundSource->Play(m_Sounds.At(0).SoundPtr, m_Sounds.At(0).SoundFrequency);
    }

    m_bIsPlaying=true;

    return true;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:12:29 UTC | #2

I also tried this.

[code]#include "CubeOpenBoxClientStd.h"

#include "AlphaEngine/Database/AlphaDatabase.h"

#include "AlphaEngine/GameLogic/BaseGameLogic.h"
#include "AlphaEngine/EventManager/Event/Server/ServerEvent.h"
#include "AlphaEngine/EventManager/Event/Client/ClientEvent.h"
#include "AlphaEngine/EventManager/Event/Request/RequestEvent.h"

#include "AlphaEngine/GameLogic/PlayerManager/HeroManager/HeroManager.h"
#include "SoundManager.h"

bool SoundManager::m_bIsInstantiated = false;

SoundManager::SoundManager(Context* context) : Object(context)
    ,m_bInitialized(false)
    ,m_bCurrentSound(0)
    ,m_pScene(NULL)
{
    // Fail if want to construct more than one SoundManager
    assert(!m_bIsInstantiated);

    // Flag generated
    m_bIsInstantiated = true;

    // Set defaults - not need but to be safe;
    m_bInitialized=false;
    m_bCurrentSound=0;
    m_pScene=NULL;

    // Get the game logic
    m_pGameLogic = g_pApp->GetGameLogic();
    m_pAudio = g_pApp->GetSubsystem<Audio>();

    return;
}

SoundManager::~SoundManager()
{
    // Prototype
    // Stop all sounds
    m_pAudio->Stop();

    return;
}

// Initialize
bool SoundManager::Initialize(void)
{
    // Initialize Delegates
    InitializeAllDelegates();

    // Initialize Sound SOurce
    m_pSoundSource = new SoundSource(context_);

    // Set source type
    m_pSoundSource->SetSoundType(SOUND_MUSIC);

    // Add sound source
    m_pAudio->AddSoundSource(m_pSoundSource);

    // Stop all sounds
    m_pAudio->Stop();

    // Set Initialize state to true
    m_bInitialized = true;

    // Master Gain
    m_pAudio->SetMasterGain(SOUND_MUSIC, 1.0f);
    m_pAudio->SetMasterGain(SOUND_EFFECT,1.0f);

    return true;
}

// Initialize all delegates
void SoundManager::InitializeAllDelegates(void)
{
    return;
}

// Handle VUpdate
void SoundManager::VOnUpdate(float timeStep)
{

    if(!m_bInitialized&&!m_bIsInstantiated)
    {
        //   ALPHAENGINE_LOGINFO("Not Initialized");
        return;
    }

    if(m_bUpdating||!m_pScene)
    {
        return;
    }

    // Is Playing
    if(m_bIsPlaying)
    {
        if(!m_pSoundSource->IsPlaying())
        {
            // if sounds exist
            if(m_Sounds.Size()>0)
            {
                // increase current sound
                m_bCurrentSound++;

                // if sound is above loaded sounds
                if(m_bCurrentSound>=m_Sounds.Size())
                {
                    // play first sound
                    m_bCurrentSound=0;
                }

                // Play Sound
                m_pSoundSource->Play(m_Sounds.At(m_bCurrentSound).SoundPtr,m_Sounds.At(m_bCurrentSound).SoundFrequency);
            }
        }
    }
}


bool SoundManager::LoadSoundType(String type, bool reset = true)
{
    FileSystem * fileSystem = g_pApp->GetFileSystem();

    // load from path
    XMLFile* file = g_pApp->GetConstantResCache()->GetResource<XMLFile>("Sounds/Sounds.xml");

    if (!file)
    {
        URHO3D_LOGERROR("Failed to load hero data from xml file");
        return false;
    }

    //Get Root
    XMLElement root = file->GetRoot();

    // stop all Sound
    m_bIsPlaying = false;
    m_bUpdating = true;

    // Verify first child
    if (root)
    {
        // Get a sound node
        XMLElement NextNode = root.GetChild("Sound");

        // Test each one
        do
        {
            // Test if a type exist and path
            XMLElement TypeNode = NextNode.GetChild("Type");
            XMLElement PathNode = NextNode.GetChild("Path");
            XMLElement FrequencyNode = NextNode.GetChild("Frequency");

            // if type is not null and path
            if(TypeNode.NotNull()&&PathNode.NotNull())
            {
                // Get the type node
                String typestring=TypeNode.GetAttribute("value");
                String soundpath = PathNode.GetAttribute("value");

                // if type string contains type
                if(typestring.Contains(type, false)&&!soundpath.Empty())
                {
                    // create a file path
                    String fullpath = g_pApp->GetGameDataDirectory()+"/"+soundpath;

                    // continue
                    if(fileSystem -> FileExists(fullpath))
                    {
                        // get frequency
                        unsigned int frequency = 44100;

                        // if freequency not there use 44.1 as the default
                        if(FrequencyNode.NotNull())
                        {
                            frequency = FrequencyNode.GetFloat("value");
                        }

                        // load resource
                        Sound * newSound = g_pApp->GetConstantResCache()->GetResource<Sound>(soundpath);

                        // Set sound looped
                        newSound->SetLooped(false);

                        // push new sound
                        if(newSound)
                        {
                            // Add sound a default frequency
                            m_Sounds.Push({newSound, newSound->GetFrequency()});
                        }
                    }
                    else
                    {
                        ALPHAENGINE_LOGINFO(fullpath);
                    }
                }
            }
        }
        while(NextNode =  NextNode.GetNext("Sound"));
    }

    // Reset Updating
    m_bUpdating = false;


    return true;
}

bool SoundManager::SetScene(Scene * setscene)
{
    // Set Scene
    m_pScene = setscene;

    // Add Music Node
    m_pMusicNode = m_pScene -> CreateChild("Music");
    m_pMusicNode->AddComponent(m_pSoundSource,0, LOCAL);

}


bool SoundManager::Play(void)
{
    if(!m_bInitialized||!m_pScene||m_bIsPlaying||m_bUpdating)
    {
        // Error message
        ALPHAENGINE_LOGINFO("Error Occurred");

        return false;
    }

    if(m_Sounds.Size()>0)
    {
        // play
        m_pAudio->Play();

        // Reset sounds to 0
        m_bCurrentSound = 0;

        // Sound
        m_pSoundSource->Play(m_Sounds.At(0).SoundPtr, m_Sounds.At(0).SoundFrequency);
    }

    m_bIsPlaying=true;

    return true;
}
[/code]

-------------------------

