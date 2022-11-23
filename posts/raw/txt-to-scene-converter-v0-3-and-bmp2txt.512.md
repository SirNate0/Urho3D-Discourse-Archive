lexx | 2017-01-02 01:01:00 UTC | #1

I made a little converter which converts .txt map file to urho3d scene .xml file.

txt2scene compiled .exe and sourcecodes: [dropbox.com/s/wn0uqkr0ry2xe ... rc.7z?dl=0](https://www.dropbox.com/s/wn0uqkr0ry2xe05/txt2scene_src.7z?dl=0)
bmp2txt compiled .exe and sourcecodes:  [dropbox.com/s/fieybrfh62bg5 ... xt.7z?dl=0](https://www.dropbox.com/s/fieybrfh62bg5qs/bmp2txt.7z?dl=0)

.txt map fileformat:
[code]
# test map file

mapSize: 15 7
blockSize: 1 1
model: 0 empty
model: 1 Plane
model: 2 Pyramid 0.2 4.0 0.2
model: 3 Sphere  0.5 0.5 0.5
model: 5 Box     1.0 2.0 1.0
model: x Torus

:floor
111111111111111
111111111111111
111111111111111
111111111111111
111111111111111
111111111111111
111111111111111

:wall
555555555555555
520002520000025
500000500333005
500x00500333005
500000000000005
52x3x252003x025
555555555555555

[/code]
(I succesfully loaded above map (converted with txt2scene) to urho3d editor, no materials though)

model names are filenames without extension, ie
  model: 3 Sphere    is     Models/Sphere.mdl

One can setup scale values to models ie
   model: 3 Sphere  [b]0.5 0.5 0.5[/b]

model: 0 empty  <-- when empty, converter doesnt create node

:layerName      <-- one can create multiple layers


Usage:      txt2scene  myskene.txt  out.xml
   txt2scene     -- binary 
   myskene.txt -- map file descripted before
   out.xml        -- urho3d scene, one can load this in editor

TODO:
* better material handling? now it uses same material name as model name (ie  Sphere.mdl uses Sphere.xml material)

ADDED:
* node names


txt2scene.cpp :
[code]
/*
txt2scene
by mjt, 2014

Converts .txt map file to urho3d scene .xml file.

*/
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

class ModelInfo
{
public:
	char name[100];
	char ch;
	float xs, ys, zs;
};
ModelInfo modelInfo[1000];

void main(int argc, char **argv)
{
	if(argc<3)
	{
		printf("txt2scene by mjt, 2014\n");
		printf("Usage:\n %s  txtMapFileName  outputSceneFileName\n", argv[0]);
		return;
	}

	// open txt map file
	FILE *in=fopen(argv[1], "r");
	if(!in)
	{
		printf("Cannot open %s\n", argv[1]);
		return;
	}

#define MAX 1000
	char line[MAX];
	char mapName[MAX];
	int modelCounter=0;
	int width=0, height=0, blockWidth=0, blockHeight=0;
	float curX=0, curZ=0;
	string data=
		"<?xml version=\"1.0\"?>\n" \
		"<scene id=\"1\">\n" \
		"   <attribute name=\"Name\" value=\"\" />\n" \
		"   <attribute name=\"Time Scale\" value=\"1\" />\n" \
		"   <attribute name=\"Smoothing Constant\" value=\"50\" />\n" \
		"   <attribute name=\"Snap Threshold\" value=\"5\" />\n" \
/*		"   <attribute name=\"Elapsed Time\" value=\"7.3882\" />\n" \
		"   <attribute name=\"Next Replicated Node ID\" value=\"15\" />\n" \
		"   <attribute name=\"Next Replicated Component ID\" value=\"24\" />\n" \
		"   <attribute name=\"Next Local Node ID\" value=\"16777222\" />\n" \
		"   <attribute name=\"Next Local Component ID\" value=\"16777217\" />\n" \  
		"   <attribute name=\"Variables\" />\n" \
		"   <attribute name=\"Variable Names\" value=\"\" />\n" \  */
		"   <component type=\"Octree\" id=\"1\" />\n" \
		"   <component type=\"DebugRenderer\" id=\"2\" />\n";


	mapName[0]=0;
	int nodeID=1, compID=1;

	while(1)
	{
		if(fgets(line, MAX, in)==0)
			break;
		if(line[0]==0) 
			break;

		if(line[0]=='\n')
			continue;
		if(line[0]=='#') // comment
			continue;

		// map size
		if(memcmp(line, "mapSize:", 8)==0)
		{
			sscanf(line, "mapSize: %d %d", &width, &height);
			printf("mapSize: %d %d\n", width, height);

			continue;
		}

		if(memcmp(line, "blockSize:", 10)==0)
		{
			sscanf(line, "blockSize: %d %d", &blockWidth, &blockHeight);
			printf("blockSize: %d %d\n", blockWidth, blockHeight);

			continue;
		}

		// model name
		if(memcmp(line, "model:", 6)==0)
		{
			float xs=1, ys=1, zs=1;
			sscanf(line, "model: %c %s %f %f %f", 
				&modelInfo[modelCounter].ch, modelInfo[modelCounter].name, &xs, &ys, &zs);

			modelInfo[modelCounter].xs=xs;
			modelInfo[modelCounter].ys=ys;
			modelInfo[modelCounter].zs=zs;
			printf("model: %c = %s  (%8.2f, %8.2f, %8.2f)\n", 
				modelInfo[modelCounter].ch, modelInfo[modelCounter].name, xs, ys, zs);
		
			modelCounter++;

			continue;
		}

		// map name (ie floor, walls, furnitures)
		if(line[0]==':')
		{
			if(mapName[0]!=0)
				data+="   </node>\n";

			sscanf(line, ":%s\n", mapName);
			printf("name: %s\n", mapName);

			curX= -((float)width * (float)blockWidth)/2;
			curZ= -((float)height * (float)blockHeight)/2;

			char temp[100];
			sprintf(temp, "   <node id=\"%d\">\n", nodeID++);
			data+=temp;

			sprintf(temp, "   <attribute name=\"Name\" value=\"%s\" />\n", mapName);
			data+=temp;

			continue;
		}

		// parse map data
		for(int w=0; w<width; w++)
		{
			char *modelName="";
			float sx=1, sy=1, sz=1;
			for(int c=0; c<modelCounter; c++)
			{
				if(modelInfo[c].ch == line[w])
				{
					modelName = modelInfo[c].name;
					sx=modelInfo[c].xs;
					sy=modelInfo[c].ys;
					sz=modelInfo[c].zs;
					break;
				}
			}

			// dont add empty nodes
			if(memcmp(modelName, "empty", 5)==0)
			{
				curX += (float)blockWidth;
				continue;
			}

			char dta[10000];
			sprintf(dta, 
				"      <node id=\"%d\">\n" \
				"         <attribute name=\"Is Enabled\" value=\"true\" />\n" \
				"         <attribute name=\"Name\" value=\"%s\" />\n" \
				"         <attribute name=\"Position\" value=\"%8.2f %8.2f %8.2f\" />\n" \
				"         <attribute name=\"Rotation\" value=\"1 0 0 0\" />\n" \
				"         <attribute name=\"Scale\" value=\"%8.2f %8.2f %8.2f\" />\n" \
				"         <component type=\"StaticModel\" id=\"%d\">\n" \
				"            <attribute name=\"Model\" value=\"Model;Models/%s.mdl\" />\n" \
				"            <attribute name=\"Material\" value=\"Material;Materials/%s.xml;\" />\n" \
				"         </component>\n" \
				"      </node>\n",
					nodeID,
					modelName,
					curX, 0.f, curZ,
					sx, sy, sz,
					compID,
					modelName,
					modelName // material name
					);

			data = data + dta;

			nodeID++;
			compID++;

			curX += (float)blockWidth;
		}

		curX = -((float)width * (float)blockWidth)/2;
		curZ += (float)blockHeight;
	}

	fclose(in);

	data+= "   </node>\n";
	data+= "</scene>\n";

	// open output file
	FILE *out=fopen(argv[2], "w");
	if(!out)
	{
		printf("Cannot create %s\n", argv[1]);
		return;
	}
	fputs(data.c_str(), out);
	fclose(out);

}

[/code]


[b]NOTES:[/b]
Making txt maps can be slow so [eggdrop.ch/projects/bmp2txt/index_en.htm](http://eggdrop.ch/projects/bmp2txt/index_en.htm)
program what I just found (not made by me) converts 24-bit .bmp -> text, so making maps with Paint
is possible (might need some modifications if using lots of different colors(objects)).
[b]EDIT:[/b] modified bmp2txt.cpp (can take 3 parameter, input_24bit.bmp output_mapfile.txt  first_letter(which to use when creating .txt))

[code]
/* bmp2txt v0.1 Copyright (C) 2003 tomasliq <tom@eggdrop.ch>
 * 
 * A very simple bmp to text converter
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */
// modified by mjt

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	FILE *file;
	unsigned short int filetype;
	long int offbits;
	int width, height;
	short int planes;
	short int bits;
	unsigned char *data, *linebuf;
	long size;
	char *outFileName="out.txt";
	char firstLetter='a';

	if (argc < 2)
	{
		printf("Usage: %s <bitmap>  (outFileName) (firstLetter) \n", argv[0]);
		exit(1);
	}
	if(argc>=3)
		outFileName=argv[2];

	if(argc>=4)
		firstLetter=argv[3][0];


	if ((file = fopen(argv[1], "rb")) == NULL)
	{
		printf("Error: Can not open file %s for reading\n", argv[1]);
		exit(1);
	}

	if (!fread(&filetype, sizeof(short int), 1, file))
	{
		printf("Error: Cannot read filetype\n");
		exit(1);
	}

	if (filetype != 19778)
	{
		printf("Error: This is not a bitmap file\n");
		exit(1);
	}
	
	fseek(file, 8, SEEK_CUR);

	if (!fread(&offbits, sizeof(long int), 1, file))
	{
		printf("Error: Cannot read offset\n");
		exit(1);
	}

	fseek(file, 4, SEEK_CUR);

	fread(&width, sizeof(int), 1, file);
	fread(&height, sizeof(int), 1, file);
	
	fread(&planes, sizeof(short int), 1, file);
	
	if (planes != 1)
	{
		printf("Error: Number of planes must be 1\n");
		exit(1);
	}

	if (!fread(&bits, sizeof(short int), 1, file))
	{
		printf("Error: Cannot read bits\n");
	}

	if (bits != 24)
	{
		printf("Error: Number of bits per pixel must be 24\n");
		exit(1);
	}

	size = width*height*3;

	linebuf = (unsigned char *)malloc(width*3);
	
	if ((data = (unsigned char *)malloc(size)) == NULL)
	{
		printf("Error: Cannot allocate memory\n");
		exit(1);
	}

	
	fseek(file, offbits, SEEK_SET);
	
	if (!fread(data, size, 1, file))
	{
		printf("Error: Cannot read bitmap data\n");
		exit(1);
	}

	fclose(file);

	FILE *out = fopen(outFileName, "w");
	if(!out)
	{
		printf("Error: Can not open file %s for writing\n", argv[1]);
		exit(1);
	}

	int difcols=1;
	long ch[1000];   // different characters
	long cols[1000]; // different colors
	cols[0]=cols[1]=cols[2]=0;
	ch[0]=' ';

	// convert colors to characters
	int x,y;
	for (y=(height-1)*3; y>0; y-=3)
	{
		for (x=0; x<width*3; x+=3)
		{
			long pos=y*width + x;
			long c = (data[pos]<<16) + (data[pos+1]<<8) + data[pos+2];


			int cc=0;
			char found=0;
			// check color
			for(cc=0; cc<difcols; cc++)
			{
				if(cols[cc]==c)
				{
					found=1;
					break;
				}
			}

			if(found)
			{
				fprintf(out, "%c", ch[cc]);
			}
			else
			{
				ch[difcols]=firstLetter + (difcols-1);
				cols[difcols]=c;

				fprintf(out, "%c", ch[difcols]);
				difcols++;
			}

		}
		fprintf(out, "\n");
	}
	free(data);
	fclose(out);

	return 0;
}
[/code]

-------------------------

