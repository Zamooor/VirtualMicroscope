#version 330
// shader003.vert

//////////////// Inputs to shader ////////////////
// Uniforms:
uniform mat4 modelMatrix;
uniform mat4 preRotationMatrix;
uniform mat4 translationMatrix;
uniform mat4 postRotationMatrix;
uniform mat4 projectionMatrix;
uniform float focalDistance;

// Vertex buffers:
in vec2 texCoord;
in vec4 position;
in vec4 normal;

////////////////////////////////////////////////

// Interpolated attributes:
out vec4 modelPosition;
out vec4 worldPosition;
out vec4 fragmentNormal;
out vec2 fragmentTexCoord;
out vec4 eye;
out vec4 pos;
out float fragmentFocalDistance;

// Locals

// These are sorted in z, so we can use blending transparency

float[60] randomVert = float[60](
-0.9712 , -0.2410 , -1.9874 ,
0.6473 , 0.6743 , -1.4156 ,
0.6095 , -0.6092 , -1.3392 ,
1.1916 , 0.3830 , -1.3200 ,
-0.3571 , 0.4169 , -1.0493 ,
2.7988 , -0.0083 , -0.9111 ,
-0.2446 , 0.5045 , -0.8563 ,
0.0536 , -0.3166 , -0.8092 ,
-1.1326 , -0.7778 , -0.8073 ,
0.9802 , -2.7329 , -0.7411 ,
-0.4324 , 1.0207 , -0.3177 ,
-0.4858 , 1.6161 , -0.2869 ,
-0.1940 , 1.4653 , 0.1119 ,
1.4027 , 0.4520 , 0.1898 ,
-1.4300 , -1.0641 , 0.2554 ,
0.5641 , 0.4661 , 0.3061 ,
0.7351 , -0.5179 , 0.8650 ,
0.7954 , 1.0387 , 0.9356 ,
-1.7899 , 0.6660 , 0.9609 ,
-0.6522 , -1.2584 , 2.0574 
);


void main()
{

    fragmentTexCoord = texCoord;
    pos = position;
    float factor = 2.0;
    int id = gl_InstanceID;
    pos.x += factor*randomVert[(id*3)%60];
    pos.y += factor*randomVert[(id*3+1)%60];
    pos.z += factor*randomVert[(id*3+2)%60];

    mat4 viewMatrix = postRotationMatrix * translationMatrix * preRotationMatrix;
    mat4 mvMatrix = viewMatrix * modelMatrix;
    fragmentNormal = mvMatrix * normal;
    worldPosition = mvMatrix * pos;
    modelPosition = position;
    eye = -normalize(vec4(worldPosition.xyz, 0.0));
    
    float dist = length(worldPosition.xyz);
    dist = (focalDistance - dist)/2.0;
    fragmentFocalDistance = clamp(abs(dist), 0.0, 1.0);

    // Magic variable to tell OpenGL where the vertex is:
    gl_Position = projectionMatrix * worldPosition;
}
