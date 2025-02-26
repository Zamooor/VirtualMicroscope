#version 330
// shader001.vert

//////////////// Inputs to shader ////////////////
// Uniforms:
uniform mat4 modelMatrix;
uniform mat4 preRotationMatrix;
uniform mat4 translationMatrix;
uniform mat4 postRotationMatrix;
uniform mat4 projectionMatrix;

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

// Locals

float[100] random = float[100](
 -0.12366357,  1.58957737, -1.07722578, -0.52129046, -0.89182673, -0.49768628,
 -1.43332240,  0.70111927, -1.62698454, -0.86845953, -1.41838148, -1.04809894,
  0.17677887, -0.53513184,  2.02827024,  0.38896931, -0.92447265, -0.77640911,
 -0.36048778,  0.66232117, -1.82117109,  0.14146804,  0.12782277,  1.62889136,
 -0.35672268, -2.07543628, -0.14985717,  0.59426944,  1.43636502, -1.05579884,
  2.39079593, -0.28016912, -1.00773986,  0.88028855, -0.47859493, -0.49425260,
  2.94291566,  1.77033828,  0.25876606,  0.44438808, -0.92950547,  0.09713399,
 -0.06339161, -0.34261976,  0.50933399,  1.85950480,  0.75108005, -1.10328051,
  0.60352673,  0.12434301,  0.72301809, -0.11667232, -0.96326365,  0.38364996,
 -0.05756680, -1.15783708, -1.71514476, -2.32726499,  0.33437245,  0.64672371,
  0.80135049,  1.22502464, -0.60502388,  0.50420500, -0.15341545, -0.02648843,
  0.07718586,  1.08380173,  0.45109420,  0.91572279,  0.81490185, -0.38737013,
  0.09908682, -0.52281031,  0.12577123, -0.18157470, -0.63671652,  0.84404271,
  0.96623124,  2.47063595,  1.94948581,  0.19885808, -0.19333715,  1.20306318,
  0.33086985,  1.71710860,  0.24243551,  0.29738248, -0.50658864, -1.16769872,
  1.34933371, -1.41718232,  0.45905715, -0.64480513,  1.60374902,  1.17327061,
  0.36985231, -0.59956504, -0.95265575, -0.14068632);

void main()
{
    fragmentTexCoord = texCoord;
    vec4 pos = position;
    float factor = 3.0;
    pos.x += factor*random[(gl_InstanceID*3)%100];
    pos.y += factor*random[(gl_InstanceID*3+1)%100];
    pos.z += factor*random[(gl_InstanceID*3+2)%100];
    mat4 viewMatrix = postRotationMatrix * translationMatrix * preRotationMatrix;
    mat4 mvMatrix = viewMatrix * modelMatrix;
    fragmentNormal = mvMatrix * normal;
    worldPosition = mvMatrix * pos;
    modelPosition = position;
    eye = -normalize(vec4(worldPosition.xyz, 0.0));

    // Magic variable to tell OpenGL where the vertex is:
    gl_Position = projectionMatrix * worldPosition;
}
